from ldap3 import SUBTREE, BASE
from directory.objects import Objects, ObjectsList, ObjectType, Object
import exceptions


class search(Objects.SEARCH):
	def user(self,query):
		objtype = {
			'objectClass' : ['top','person', 'organizationalPerson', 'user']
		}
		return self._get(query)

	def group(self,query):
		objtype = {
			'objectClass' : ['top', 'group']
		}
		return self._get(query)

	def computer(self,query):
		objtype = {
			'objectClass' : ['top','person', 'organizationalPerson', 'user']
		}
		return self._get(query)

	def ou(self,query):
		objtype = {
			'objectClass' : ['top', 'organizationalUnit']
		}
		return self._get(query)

	def _get(self,query):
		attributes = ['*','+']
		searchScope = SUBTREE
		result = ObjectsList(Object,self._engine)
		c = self._engine._worker
		cookie = None
		while (cookie) or (cookie == None):
			c.search(search_base=self._engine._settings.basedn,search_filter=query,search_scope = SUBTREE, attributes=['*','+'], paged_size=1000, paged_cookie=cookie)
			cookie = c.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
			for entry in c.response:
				if not 'dn' in entry.get('raw_attributes',{'dn':False}):
					entry['raw_attributes']['dn'] = entry['raw_attributes']['distinguishedName']
				if not entry.get('uri',False):
					result.append(entry['raw_attributes'])
		return result

class get(search):
	def _get(self,query):
		result = super(get,self)._get(query)
		if len(result) > 1:
			raise exceptions.MultipleResults
		return result[0]


class objects(Objects):
	_search = search
	_get = get
