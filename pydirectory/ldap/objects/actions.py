from directory.objects import actions
from ldap3 import SUBTREE, BASE
import importlib

class search (actions.search):
	def object(self,*args,**kwargs):
		return self.__call__(*args,**kwargs)

	def _get(self,query,**kwargs):
		scope = SUBTREE
		if kwargs.get('scope','').upper() == 'BASE':
			scope = BASE

		if kwargs.get("dn",False):
			basedn=kwargs["dn"]
		else:
			basedn=self._objects._engine._settings.basedn
		if (query == None):
			if kwargs.get("dn",False):
				query = '(objectclass=*)'
			else:
				raise self._exceptions.LDAPInvalidFilterError("must be set query filter syntax")

		attributes = ['*','+']
		searchScope = SUBTREE
		c = self._objects._engine._worker
		cookie = None
		while (cookie) or (cookie == None):
			try:
				c.search(search_base=basedn,search_filter=query,search_scope = scope, attributes=['*','+'], paged_size=1000, paged_cookie=cookie)
			except self._exceptions.LDAPSocketSendError:
				self._objects._engine.login()
				c.search(search_base=basedn,search_filter=query,search_scope = scope, attributes=['*','+'], paged_size=1000, paged_cookie=cookie)

			if not (c.result.get('result',False) == 0):
				code = c.result.get('result')
				if code == 10:
					raise self._exceptions.LDAPReferrals(c.result['referrals'][0])
				raise self._exceptions.LDAPError(str(c.result))
			cookie = c.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
			for entry in c.entries:
				entry._response['raw_attributes']['dn'] = [entry._dn]
				try:
					entry._response['raw_attributes']['container'] = [",".join(entry._response['raw_attributes']['dn'][0].split(',')[1:])]
				except TypeError: #python 3.0 compatibility
					entry._response['raw_attributes']['container'] = [b",".join(entry._response['raw_attributes']['dn'][0].split(b',')[1:])]
				self._objectslist.append(entry._response['raw_attributes'])
		return self._objectslist

class get(search):
	def _get(self,*args,**kwargs):
		result= super(get,self)._get(*args,**kwargs)
		if len(result) <= 0:
			raise self._exceptions.ObjectNotExist
		if len(result) > 1:
			raise self._exceptions.MultipleResults
		return result[0]

class new (actions.new):
	def _get(self,data,*args,**kwargs):
		self._objectslist.append(data)
		return self._objectslist[0]
