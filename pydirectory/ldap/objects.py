from ldap3 import SUBTREE, BASE
from directory.objects import Objects, ObjectsList, Object

class objects(Objects):
	def search(self,query):
		attributes = ['*','+']
		searchScope = SUBTREE
		result = ObjectsList(Object)
		c = self._engine._worker

		cookie = None
		while (cookie) or (cookie == None):
			c.search(search_base=self._engine._settings.basedn,search_filter=query,search_scope = SUBTREE, attributes=['*','+'], paged_size=1000, paged_cookie=cookie)
			cookie = c.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
			for entry in c.response:
				if not entry.get('uri',False):
					result.append(entry['raw_attributes'])
		return result
