from ldap.objects import types

class object(types.object):
	_type = {}

class user(object):
	_type = {
		'objectClass' : [b'top',b'person', b'organizationalPerson', b'user']
	}

class group(object):
	_type = {
		'objectClass' : [b'top', b'group']
	}

class computer(object):
	_type = {
		'objectClass' : [b'top',b'person', b'organizationalPerson', b'user', b'computer']
	}

class ou(object):
	_type = {
		'objectClass' : [b'top', b'organizationalUnit']
	}
