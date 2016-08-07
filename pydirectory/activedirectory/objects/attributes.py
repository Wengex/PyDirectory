from ldap.objects.attributes import *
import binascii, uuid

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
			self._raw = [str(value)]

	def _tohuman(self):
		binary = bin(int(self.value))[2:][::-1]
		values = []
		for bit in range(0,len(binary)):
			if binary[bit] == '1':
				decimal = int(binary[bit]+'0'*bit,2)
				try:
					position = list(self.types.values()).index(decimal)
					value = list(self.types.keys())[position]
					values.append(value)
				except:
					values.append("UNKNOWN")
		return values


class unicodePwd(attribute):
	def _toraw(self,value):
		try:
			password = ('"%s"' % value).encode('utf-16-le')
		except UnicodeDecodeError:
			password = ('"%s"' % value.decode('utf-8')).encode('utf-16-le')
		self._raw = [password]

	def _tohuman(self):
		raise self._exceptions.PasswordPrintNotAllowed


class ObjectSid(attribute):
	_is_readonly = True

	def _littleEndian(self,hex):
		result = '';
		xinit = len(hex) - 2
		for x in range(xinit,0-1,-2):
			result += hex[x:x+2]
		return result

	def _getTextSID(self,binsid):
		hex_sid = binascii.hexlify(binsid).decode('utf-8')
		subcount = int(hex_sid[2:2+2],16)
		rev = int(hex_sid[0:0+2],16)
		auth = int(hex_sid[4:4+12],16)
		result = str(rev)+'-'+str(auth)
		subauth = {}
		for x in range(0,subcount):
			le = hex_sid[16+(x*8):(16+(x*8))+8]
			subauth[x] = int(self._littleEndian(le),16)
			try:
				result += '-'+str(subauth[x])
			except TypeError:
				result += '-'+bytes(subauth[x])
		return 'S-'+result

	def _tovalue(self):
		return self._getTextSID(self.raw[0])


class sIDHistory(ObjectSid):
	pass


class ObjectGUID(attribute):
	_is_readonly = True
	def _tovalue(self):
		return str(uuid.UUID(bytes=self.raw[0]))
