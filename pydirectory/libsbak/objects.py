class ObjectTypes(object):
	class base(str):
		pass

	def __call__(self,field,value):
		try:
			var = getattr(self,field)(value)
		except:
			var = getattr(self,'base')(value)
		return var

	def __init__(self):
		super(ObjectTypes,self).__init__()



class Object(object):
	__nofields = ['types']
	def __getitem__(self,name):
		return self.__dict__[name]

	def __setitem__(self,field,value):
		setattr(self,field,value)


	def __init__(self,data):
		self.types = ObjectTypes()

		if not (type(data) == dict):
			raise exceptions.AttributeNotValid("Data to append is not a Dict")

		for key,value in data.items():
			setattr(self,key,value)

	def __setattr__(self,field,value):
		field = field.lower()
		if not (field in self.__nofields):
			super(Object,self).__setattr__(field,self.types(field,value))
		else:
			super(Object,self).__setattr__(field,value)


class ObjectList (list):

	def __init__(self,*args,**kwargs):
		super(ObjectList,self).__init__(*args,**kwargs)

	def append(self,data):
		data = Object(data)
		super(ObjectList,self).append(data)
