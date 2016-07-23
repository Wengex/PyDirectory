import exceptions

class Option(object):
	def __init__(self,null=True,value=None,type=None,validator=None,description=None):
		self.__null = null
		self.__type = type
		self.__validator = validator
		self.__description = description
		self.value = value

	def __str__(self):
		result = self.value
		if self.value == None:
			result = ''
		return result

	def __repr__(self):
		return self.__str__()

	def __setattr__(self,name,value):
		if name == "value":
			if value != None:
				if self.__type != None:
					if type(value) != self.__type:
						raise exceptions.InvalidValueType
				if self.__validator != None:
					if not self.__validator(value):
						raise exceptions.InvalidValue

		super(Option,self).__setattr__(name,value)


class Settings(object):
	def options(self):
		pass

	def __init__(self,**kwargs):
		self.options()

	def __setattr__(self,name,value):
		if self.__dict__.get(name,False):
			self.__dict__[name].value = value
		else:
			if type(value) != Option:
				raise exceptions.MustBeOptionType
			super(Settings,self).__setattr__(name,value)
