import importlib
import directory.objects.types


class objecttypes(object):
	def __init__(self,engine):
		self._engine = engine

	def _getobject(self,value):
		return importlib.import_module("%(type)s.objects.types" % {'type':self._engine._settings.type}).object(self._engine,value)

	def __call__(self,value):
		return self._getobject(value)

class objectslist(object):
	def __init__(self,engine): #change engine by object
		self._engine = engine
		self.objecttypes = importlib.import_module("%(type)s.objects.classes" % {'type':engine._settings.type}).objecttypes(self._engine)
		self._store = []

	def __getitem__(self,key):
		return self._store[key]

	def __setitem__(self,key,data):
		self._store[key] = self._setobject(data)

	def __delitem__(self,key):
		del self._store[key]

	def __iter__(self):
		return iter(self._store)

	def __str__(self):
		return str(self._store)

	def __repr__(self):
		return repr(self._store)

	def _setobject(self,data):
		return self.objecttypes(data)

	def append(self,data):
		self._store.append(self._setobject(data))

class objects(object):
	def __init__(self,engine):
		self._exceptions = importlib.import_module("%(type)s.exceptions" % {'type':engine._settings.type})
		self._engine = engine
		self._search = importlib.import_module("%(type)s.objects.actions" % {'type':engine._settings.type}).search
		self._get = importlib.import_module("%(type)s.objects.actions" % {'type':engine._settings.type}).get
		self._new = importlib.import_module("%(type)s.objects.actions" % {'type':engine._settings.type}).new

	@property
	def search(self):
		return self._search(self._engine)

	@property
	def get(self):
		return self._get(self._engine)

	def new(self):
		return self._new(self._engine)