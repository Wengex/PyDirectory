class attribute(object):
	def __init__(self,engine,attribute):
		self._engine = engine
		self.raw = attribute
		self._type_save = 'REPLACE'

	@property
	def value(self):
		if len(self.raw) <= 1:
			return self.raw[0]
		else:
			return self.raw

	def __getitem__(self,key):
		return self.raw[key]

	def __setitem__(self,key,value):
		self.raw[key] = value

	def __setattr__(self,key,value):
		super(attribute,self).__setattr__(key,value)


	def __str__(self):
		return self.value.__str__()

	def __repr__(self):
		return self.value.__repr__()


class cn(attribute):
	pass
