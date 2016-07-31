class attribute(object):
	def __init__(self,value,modify=True):
		self._is_modified = False
		self._is_append = False
		self._is_delete = False
		self._delattr = []
		self._addattr = []
		if not (type(value) == list):
			self._raw = [value]
		else:
			self._raw = value

		if modify:
			self._is_modified = True
		else:
			self._is_modified = False

	def __str__(self):
		if type(self.value) == str:
			return self.value
		else:
			return str(self.value)

	def __repr__(self):
		if type(self.value) == str:
			return self.value
		else:
			return repr(self.value)

	def __setitem__(self,key,value):
		self._raw[key] = value

	def __getitem__(self,key):
		return self._raw[key]

	def __delitem__(self,key):
		value = self._raw[key]
		self._delattr.append(value)
		self._is_delete = True

	def __iter__(self):
		return iter(self._raw)

	def append(self,value):
		self._addattr.append(value)
		self._is_append = True

	@property
	def value(self):
		if len(self._raw) == 1:
			if type(self._raw[0]) == bytes:
				return self._raw[0].decode('utf-8')
			return self._raw[0]
		return self._raw

	@property
	def raw(self):
		return self._raw
