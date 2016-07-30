import importlib

class search(object):
	def __init__(self,engine):
		self._engine = engine
		self._objectslist = importlib.import_module("%(type)s.objects.classes" % {'type':self._engine._settings.type}).objectslist(self._engine)

	def __call__(self,query):
		return self._get(query)

class new(object):
	def __init__(self,engine):
		self._engine = engine

	def __call__(self,query):
		return self._get(query)
