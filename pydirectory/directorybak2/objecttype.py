class Object(object):
	attributes = directory.attributes
	def __init__(self,engine,data):
		self._store = dict()
		self._engine = engine
		self._update(data)
		self._delete = []

	def _update(self,data):
		for attr,value in data.items():
			self[attr] = value

	def __setattr__(self,key,value):
		if key.find('_') == 0:
			super(Object,self).__setattr__(key,value)
		else:
			self.__setitem__(key,value)

	def __delattr__(self,key):
		if key.find('_') == 0:
			super(Object,self).__delattr__(value)
		else:
			self._delete.append(key)
			del self._store[key]

	def __getattr__(self,key):
		if key.find('_') == 0:
			return super(Object,self).__getattribute__(key)
		return self._store[key]

	def __setitem__(self,key,value):
		try:
			self._store[key] = getattr(self.attributes,key.lower())(self._engine,value)
		except AttributeError:
			self._store[key] = self.attributes.attribute(self._engine,value)

	def __dir__(self):
		return self._store.keys()

	def __getitem__(self,key):
		return self._store[key]

	def __delitem__(self,key):
		del self._store[key]

	def __len__(self):
		return len(self._store)

	def __iter__(self):
		return iter(self._store)

	def save(self):
		pass
