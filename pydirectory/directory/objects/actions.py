import importlib

class search(object):
	def __init__(self,objects):
		self._objects = objects
		self._objectslist = importlib.import_module("%(type)s.objects.classes" % {'type':self._objects._engine._settings.type}).objectslist(self._objects)

	def __call__(self,query):
		return self._get(query)

class new(object):
	def __init__(self,objects):
		self._objects = objects

	def __call__(self,query):
		return self._get(query)
