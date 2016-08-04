from ldap.objects import types

class object(types.object):
	type = {}

class user(object):
	type = {
		'objectClass' : [b'top',b'person', b'organizationalPerson', b'user']
	}

class group(object):
	type = {
		'objectClass' : [b'top', b'group']
	}

class computer(object):
	type = {
		'objectClass' : [b'top',b'person', b'organizationalPerson', b'user', b'computer']
	}

class ou(object):
	type = {
		'objectClass' : [b'top', b'organizationalUnit']
	}
