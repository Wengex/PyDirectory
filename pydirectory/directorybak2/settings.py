import socket
import exceptions
import getpass

class Option(object):
	def __init__(self,null=True,value=None,is_password=False,is_hostname=False,type=None,validator=None,description=None):
		self.null = null
		self.__type = type
		self.is_password=is_password
		self.is_hostname=is_hostname
		self.__validator = validator
		self.__doc__ = description
		if value == None:
			if not self.null:
				self._input_text()
			else:
				self.value = value
		else:
			self.value = value

	def _input_text(self):
		if self.is_password:
			self.value=getpass.getpass(self.__doc__+': ')
		else:
			self.value=input(self.__doc__+': ')


	def __str__(self):
		result = self.value
		if self.value == None:
			result = 'None'
		if self.is_password:
			raise exceptions.PasswordPrintNotAllowed
		return result

	def __eq__ (self,other):
		return self.value == other

	def __repr__(self):
		if type(self.value) == bytes:
			return self.value
		if self.is_password:
			return str(self.value)
		return self.__str__()

	def __setattr__(self,name,value):
		if name == "value":
			if value != None:
				try:
					value = self.__type(value)
				except ValueError as e:
					raise exceptions.InvalidValueType(e)

				if self.__validator != None:
					if not self.__validator(value):
						raise exceptions.InvalidValue

			if self.is_hostname:
				try:
					self.ipv4 = socket.getaddrinfo(value,None,socket.AF_INET)[0][4][0]
				except socket.gaierror:
					self.ipv4 = False

				try:
					self.ipv6 = socket.getaddrinfo(value,None,socket.AF_INET6)[0][4][0]
				except socket.gaierror:
					self.ipv6 = False

				if (not self.ipv4) and (not self.ipv6):
					raise exceptions.DNSHostnameCanNotBeResolved

		super(Option,self).__setattr__(name,value)



class Settings(object):

	def __init__(self,type,**kwargs):
		self.type = Option(null=False,type=str,description="Type engine",value=type)
		self._options(**kwargs)

	def __setattr__(self,name,value):
		if self.__dict__.get(name,False):
			self.__dict__[name].value = value
		else:
			if type(value) != Option:
				raise exceptions.MustBeOptionType
			super(Settings,self).__setattr__(name,value)
