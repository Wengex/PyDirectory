from directory.exceptions import *
from ldap3 import LDAPSocketOpenError,LDAPInvalidFilterError,LDAPChangesError,LDAPInvalidCredentialsResult

class LDAPError(customException):
	pass


class LDAPReferrals(LDAPError):
	pass
