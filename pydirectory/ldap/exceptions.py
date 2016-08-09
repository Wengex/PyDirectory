from directory.exceptions import *
from ldap3 import LDAPSocketOpenError,LDAPInvalidFilterError,LDAPChangesError,LDAPInvalidCredentialsResult
from pyasn1.error import PyAsn1Error

class LDAPError(customException):
	pass


class LDAPReferrals(LDAPError):
	pass

class DNisNone(customException):
	message = "DN is None"
