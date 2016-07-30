import importlib

class object(object):
	def __init__(self,engine,data):
		self._engine = engine
		self._attributes = importlib.import_module("%(type)s.objects.attributes" % {'type':self._engine._settings.type})
		self._attrs = {}
		self._update(data)
		self._deletes = []

	def __setitem__(self,key,value):
		try:
			attribute = getattr(self._attributes,key)
		except AttributeError:
			attribute = self._attributes.attribute
		self._attrs[key.lower()] = attribute(value)

	def __getitem__(self,key):
		return self._attrs[key]

	def __delitem__(self,key):
		self._deletes.append(key)
		del self._attrs[key]

	def __getattribute__(self,key):
		if key.find('_') == 0:
			return super(object,self).__getattribute__(key)
		return self[key]

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
		return str(self._attrs['cn'])

	def __repr__(self):
		return repr(self._attrs['cn'])

	def items(self):
		return self._attrs.items()

	def save(self):
		pass
