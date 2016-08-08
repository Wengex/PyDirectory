from collections import defaultdict
import string

class query(object):
	pass

class setQuery(object):
	operators = {
		'gt' : "({field}>{value})",
		'ge' : "({field}>={value})",
		'lt' : '({field}<{value})',
		'le' : '({field}<={value})',
		'eq' : '({field}={value})',
	}

	def is_disable(self,value):
		if value == True:
			return '(userAccountControl:1.2.840.113556.1.4.803:=2)'
		elif value == False:
			return '(!(userAccountControl:1.2.840.113556.1.4.803:=2))'

	def is_not(self,**fields):
		pass

	def is_and(self,value):
		return True

	def is_or(self,value):
		return True


	def _parser(self,**fields):
		result = ''
		for rawfield,value in fields.items():
			field = rawfield.split('__')[0]
			operators = rawfield.split('__')[1:]
			default = True
			for operator in self.operators:
				if operator in operators:
					default = False
					result += self.operators[operator].format(field=field,value=value)
		return result

	def __call__(self,**fields):
		return self._parser(**fields)
