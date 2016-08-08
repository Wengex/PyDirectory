from ldap.objects.actions import *

class search (search):
	def users(self,query=None,*args,**kwargs):
		if query != None:
			query = '(&{query}(&(objectclass=top)(objectclass=person)(objectclass=organizationalPerson)(objectclass=user)(!(objectclass=computer))))'.format(query=query)
		return self.__call__(query,*args,**kwargs)

	def groups(self,query=None,*args,**kwargs):
		if query != None:
			query = '(&{query}(&(objectclass=top)(objectclass=group)))'.format(query=query)
		return self.__call__(query,*args,**kwargs)

	def computers(self,query=None,*args,**kwargs):
		if query != None:
			query = '(&{query}(&(objectclass=top)(objectclass=person)(objectclass=organizationalPerson)(objectclass=user)(objectclass=computer)))'.format(query=query)
		return self.__call__(query,*args,**kwargs)

	def ous(self,query=None,*args,**kwargs):
		if query != None:
			query = '(&{query}(&(objectclass=top)(objectclass=organizationalUnit)))'.format(query=query)
		return self.__call__(query,*args,**kwargs)

class get(get):
	def user(self,query=None,*args,**kwargs):
		if query != None:
			query = '(&{query}(&(objectclass=top)(objectclass=person)(objectclass=organizationalPerson)(objectclass=user)(!(objectclass=computer))))'.format(query=query)
		return self.__call__(query,*args,**kwargs)

	def group(self,query=None,*args,**kwargs):
		if query != None:
			query = '(&{query}(&(objectclass=top)(objectclass=group)))'.format(query=query)
		return self.__call__(query,*args,**kwargs)

	def computer(self,query=None,*args,**kwargs):
		if query != None:
			query = '(&{query}(&(objectclass=top)(objectclass=person)(objectclass=organizationalPerson)(objectclass=user)(objectclass=computer)))'.format(query=query)
		return self.__call__(query,*args,**kwargs)

	def ou(self,query=None,*args,**kwargs):
		if query != None:
			query = '(&{query}(&(objectclass=top)(objectclass=organizationalUnit)))'.format(query=query)
		if kwargs.get('dn',False):
			kwargs['scope'] = 'BASE'
		return self.__call__(query,*args,**kwargs)

class new (new):
	pass
