from ldap.objects import types
from activedirectory.tools import OffsetTzInfo

class object(types.object):
	_type = {}

class user(object):
	_type = {
		'objectClass' : [b'top',b'person', b'organizationalPerson', b'user']
	}
	@property
	def is_enable(self):
		mod = int(self.useraccountcontrol.value) % 8
		if mod == 0:
			return True
		else:
			return False

	@property
	def is_disable(self):
		return not self.is_enable

	def enable(self):
		self.useraccountcontrol = ["NORMAL_ACCOUNT"]
		self.save()

	def disable(self):
		'''Method to disable User in Active Directory'''
		self.useraccountcontrol = ["NORMAL_ACCOUNT","ACCOUNTDISABLE"]
		self.save()

	def setPassword(self,value):
		self.unicodePwd = password
		self.save()



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
