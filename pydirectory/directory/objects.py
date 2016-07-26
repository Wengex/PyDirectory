class Object(object):
	pass

class SEARCH(object):
	def __init__(self,engine):
		self._engine = engine


		def __call__(self,query):
			return self._get(query)
class NEW(object):
	def __init__(self,engine):
		self._engine = engine

	def __call__(self,query):
		return self._get(query)

class ObjectsList(list):
	def __init__(self,object,*args,**kwargs):
		self._object = object
		super(ObjectsList,self).__init__(*args,**kwargs)

	def append(self,data):
		super(ObjectsList,self).append(data)

class Objects(object):
	def __init__(self,engine):
		self._engine = engine

	@property
	def search(self):
		return self._search(self._engine)

	@property
	def get(self):
		return self._get(self._engine)

	def new(self):
		return self._new(self._engine)
