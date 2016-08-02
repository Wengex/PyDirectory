from directory.objects import actions
from ldap3 import SUBTREE, BASE
import importlib

class search (actions.search):
	def object(self,*args,**kwargs):
		return self.__call__(*args,**kwargs)

	def _get(self,query,**kwargs):
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
			c.search(search_base=basedn,search_filter=query,search_scope = SUBTREE, attributes=['*','+'], paged_size=1000, paged_cookie=cookie)
			if not (c.result.get('result',False) == 0):
				code = c.result.get('result')
				if code == 10:
					raise self._exceptions.LDAPReferrals(c.result['referrals'][0])
				raise self._exceptions.LDAPError(str(c.result))
			cookie = c.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
			for entry in c.response:
				if not 'dn' in entry.get('raw_attributes',{'dn':False}):
					entry['raw_attributes']['dn'] = entry['raw_attributes']['distinguishedName']
				if not entry.get('uri',False):
					self._objectslist.append(entry['raw_attributes'])
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
	pass
