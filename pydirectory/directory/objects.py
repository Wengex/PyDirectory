class Objects(object):
	def __init__(self,engine):
		self._engine = engine

	def search(self,query):
		pass

	def get(self,**kwargs):
		return self.search(**kwargs)[0]
