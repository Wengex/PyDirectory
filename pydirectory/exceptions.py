
class customException(Exception):
	def __init__(self,message=False):
		if message:
			self.message=message

	def __str__(self):
		return repr(self.message)


class NotValidController(customException):
	message = "Not Valid Controller"

class InvalidServer(customException):
	message = "Invalid Host or Server Name"

class UnknownError(customException):
	message = "Unknown Error"

class InvalidCredentials(customException):
	message = "Invalid username y/or password"

class AttributeNotValid(customException):
	message = "The attribute is not valid"

class SettingsOptionNotExists(customException):
	message = "The Settings Option to set not exists"

class InvalidValueType(customException):
	message = "Invalid value type"

class InvalidValue(customException):
	message = "Invalid value"

class MustBeOptionType(customException):
	message = "Value must be Option type"
