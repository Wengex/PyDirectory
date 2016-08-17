from ldap.objects import types

class object(types.object):
	_type = {}

class user(object):
	_type = {
		'objectClass' : [b'top', b'person', b'organizationalPerson', b'user']
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

	@property
	def whenPasswordExpires(self):
		import decimal, datetime

		pwdLastSet = int(self.pwdlastset.raw[0])

		if self.useraccountcontrol.value == '66048':
			return None #Object password not expire

		if (pwdLastSet == 0):
			return 0

		try:
			maxPwdAge = int(self._objects.base.maxpwdage.raw[0])
			mod = int(maxPwdAge) % 4294967296
		except:
			mod = 0
		if mod == 0:
			return None #Domain not expire object passwords

		pwdExpire = decimal.Decimal(pwdLastSet) - decimal.Decimal(maxPwdAge)
		expiryts = int((pwdExpire / 10000000) - 11644473600)

		return datetime.datetime.fromtimestamp(expiryts)

class group(object):
	_type = {
		'objectClass' : [b'top', b'group']
	}

	def addMember(self,object):
		pass

	def delMember(self,object):
		pass

	def inGroup(self,object):
		if (object.dn != None) and (self.dn != None):
			members = self._objects.search(self._objects.setQuery(in_group=object.dn.value))
			for member in members:
				if member.dn.value.strip().lower() == self.dn.value.strip().lower():
					return True
		return False

class computer(object):
	_type = {
		'objectClass' : [b'top',b'person', b'organizationalPerson', b'user', b'computer']
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
		self.useraccountcontrol = ["PASSWD_NOTREQD","WORKSTATION_TRUST_ACCOUNT"]
		self.save()

	def disable(self):
		'''Method to disable User in Active Directory'''
		self.useraccountcontrol = ["ACCOUNTDISABLE","PASSWD_NOTREQD","WORKSTATION_TRUST_ACCOUNT"]
		self.save()

class ou(object):
	_type = {
		'objectClass' : [b'top', b'organizationalUnit']
	}
