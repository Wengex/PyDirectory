from directory.objects import attributes
from ldap3 import MODIFY_REPLACE


class attribute(attributes.attribute):
	_use_rdn = False
	_operator = MODIFY_REPLACE

class cn(attribute):
	_use_rdn = True

class samaccountname(attribute):
	pass
