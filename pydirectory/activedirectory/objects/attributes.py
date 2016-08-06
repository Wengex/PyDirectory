from ldap.objects.attributes import *


class userAccountControl(attribute):
	types = {
		"SCRIPT" : 1,
		"ACCOUNTDISABLE" : 2,
		"HOMEDIR_REQUIRED" : 8,
		"LOCKOUT" : 16,
		"PASSWD_NOTREQD" : 32,
		"ENCRYPTED_TEXT_PWD_ALLOWED" : 128,
		"TEMP_DUPLICATE_ACCOUNT" : 256,
		"NORMAL_ACCOUNT" : 512,
		"INTERDOMAIN_TRUST_ACCOUNT" : 2048,
		"WORKSTATION_TRUST_ACCOUNT" : 4096,
		"SERVER_TRUST_ACCOUNT" : 8192,
		"DONT_EXPIRE_PASSWORD" : 65536,
		"MNS_LOGON_ACCOUNT" : 131072,
		"SMARTCARD_REQUIRED" : 262144,
		"TRUSTED_FOR_DELEGATION" : 524288,
		"NOT_DELEGATED" : 1048576,
		"USE_DES_KEY_ONLY" : 2097152,
		"DONT_REQ_PREAUTH" : 4194304,
		"PASSWORD_EXPIRED" : 8388608,
		"TRUSTED_TO_AUTH_FOR_DELEGATION" : 16777216
	}

	def accountControl(self,options):
		val = 0
		for type in options:
			val = val + self.types.get(type,0)
		return val

	def _toraw(self,value):
		if type(value) == list:
			acControl = self.accountControl(value)
			if acControl > 0:
				self._raw = [str(acControl)]
			else:
				self._raw = value
		else:
			self.raw = [str(value)]

	@property
	def _tohuman(self):
		binary = bin(int(self.value))[2:][::-1]
		print (binary)
		values = []
		for bit in range(0,len(binary)):
			if binary[bit] == '1':
				decimal = int(binary[bit]+'0'*bit,2)
				try:
					position = self.types.values().index(decimal)
					value = self.types.keys()[position]
					values.append(value)
				except:
					values.append("UNKNOWN")
		return values



	#	pass
#		if type(value) == list:
#			acControl = self.adldap.accountControl(value)
#			if acControl > 0:
#				self.raw = [str(self.adldap.accountControl(value))]
#			else:
#				self.raw = value
#		else:
#			self.raw = [str(value)]
