class Object(object):
	pass

class ObjectsList(list):
	def __init__(self,object,*args,**kwargs):
		self._object = object
		super(ObjectsList,self).__init__(*args,**kwargs)

	def append(self,data):
		super(ObjectsList,self).append(data)

class Objects(object):
	def __init__(self,engine):
		self._engine = engine

	def search(self,query):
		pass

	def get(self,**kwargs):
		return self.search(**kwargs)[0]
