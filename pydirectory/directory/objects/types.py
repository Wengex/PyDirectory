import importlib

class object(object):
	objtype = {}
	def __init__(self,objects,data):
		self._objects = objects
		self._exceptions = self._objects._exceptions
		self._attributes = importlib.import_module("%(type)s.objects.attributes" % {'type':self._objects._engine._settings.type})
		self._attrs = {}
		self._initload = True
		self._update(data)
		self._initload = False
		self._deletes = []

	def __setitem__(self,key,value):
		try:
			attribute = getattr(self._attributes,key)
		except AttributeError:
			attribute = self._attributes.attribute
		if self._initload:
			self._attrs[key.lower()] = attribute(value,self._objects,modify=False)
		else:
			self._attrs[key.lower()] = attribute(value,self._objects,modify=True)

	def __getitem__(self,key):
		return self._attrs[key]

	def __delitem__(self,key):
		self._deletes.append(key)
		del self._attrs[key]

	def __getattribute__(self,key):

		if key.find('_') != 0:
			if key in self._attrs:
				return self[key]
		return super(object,self).__getattribute__(key)

	def __setattr__(self,key,value):
		if key.find('_') == 0:
			super(object,self).__setattr__(key,value)
		else:
			self[key] = value

	def __delattr__(self,key):
		if key.find('_') == 0:
			super(object,self).__delattr__(key)
		del self[key]

	def __len__(self):
		return len(self._attrs)

	def __iter__(self):
		return iter(self._attrs)

	def __dir__(self):
		return self._attrs.keys()

	def _update(self,data):
		for attr,value in data.items():
			self[attr] = value

	def __str__(self):
		return str(self._attrs['dn'])

	def __repr__(self):
		return repr(self._attrs['dn'])

	def items(self):
		return self._attrs.items()

	@classmethod
	def is_type(self,data):
		if data == self.objtype.copy():
			return True
		return False

	def save(self):
		return False

	def reset(self):
		self._delattr = []
		self._addattr = []
		self._reset()
