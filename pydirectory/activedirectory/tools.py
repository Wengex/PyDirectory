from ldap.tools import *

class setQuery(setQuery):
	specialFields = {
		'is_disable' : {
	 		True: '(userAccountControl:1.2.840.113556.1.4.803:=2)',
			False: '(!(userAccountControl:1.2.840.113556.1.4.803:=2))',
		},
		'is_enable' : {
	 		True: '(!(userAccountControl:1.2.840.113556.1.4.803:=2))',
			False: '(userAccountControl:1.2.840.113556.1.4.803:=2)',
		},
	}
