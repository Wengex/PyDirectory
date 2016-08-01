class attribute(object):
	def __init__(self,value,objects,modify=True):
		self._objects = objects
		self._exceptions = self._objects._exceptions
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
		if self._is_modified:
			raise self._exceptions.ObjectIsModified
		value = self._raw[key]
		changed = False
		if value in self._addattr:
			key = self._addattr.index(value)
			del self._addattr[key]
			changed = True
		if not value in self._delattr:
			self._delattr.append(value)
			changed = True
		if changed:
			self._is_delete = True

	def __iter__(self):
		return iter(self._raw)

	def append(self,value):
		if self._is_modified:
			raise self._exceptions.ObjectIsModified
		changed = False
		if value in self._delattr:
			key = self._delattr.index(value)
			del self._delattr[key]
			changed = True
		if not value in self._addattr:
			self._addattr.append(value)
			changed = True
		if changed:
			self._is_append = True

	@property
	def value(self):
		result = self._raw
		if not self._is_modified:
			if len(self._raw) == 1:
				if type(self._raw[0]) == bytes:
					return self._raw[0].decode('utf-8')
					result = self._raw[0]
		if self._is_append or self._is_delete:
			lsum = set(self._addattr) | set(self._raw)
			ldel = lsum - set(self._delattr)
			result = list(ldel)

		return result

	@property
	def raw(self):
		return self._raw
