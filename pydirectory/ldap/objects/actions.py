from directory.objects import actions
from ldap3 import SUBTREE, BASE
import importlib

class search (actions.search):
	def object(self,query):
		return self._get(query)

	def _get(self,query):
		attributes = ['*','+']
		searchScope = SUBTREE
		c = self._engine._worker
		cookie = None
		while (cookie) or (cookie == None):
			c.search(search_base=self._engine._settings.basedn,search_filter=query,search_scope = SUBTREE, attributes=['*','+'], paged_size=1000, paged_cookie=cookie)
			cookie = c.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
			for entry in c.response:
				if not 'dn' in entry.get('raw_attributes',{'dn':False}):
					entry['raw_attributes']['dn'] = entry['raw_attributes']['distinguishedName']
				if not entry.get('uri',False):
					self._objectslist.append(entry['raw_attributes'])
		return self._objectslist

class get(search):
	def _get(self,query):
		return super(get,self)._get(query)[0]

class new (actions.new):
	pass
