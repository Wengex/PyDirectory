from directory.exceptions import *
from ldap3 import LDAPSocketOpenError,LDAPInvalidFilterError

class LDAPError(customException):
	pass


class LDAPReferrals(LDAPError):
	pass
