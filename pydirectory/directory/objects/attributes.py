class attribute(object):
	def __init__(self,value):
		self._raw = value

	def __str__(self):
		return str(self._raw)

	def __repr__(self):
		return repr(self._raw)

	def __setitem__(self,key,value):
		self._raw[key] = value

	def __getitem__(self,key):
		return self._raw[key]

	def __iter__(self):
		return iter(self._raw)

	@property
	def value(self):
		return self._raw
