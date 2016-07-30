import exceptions
from ldap3 import Server, Connection, ALL, SUBTREE, BASE
from directory.engine import Engine

class engine (Engine):
	def _authenticate(self,username,password,login=False):
		server_options = {
		 'host': repr(self._settings.host),
		 'use_ssl': repr(self._settings.ssl),
		 'get_info': ALL
		}
		server = Server(**server_options)
		conn = Connection(server, user=username,password=password)
		result = False
		try:
			result = conn.bind()
		except ldap3.LDAPSocketOpenError:
			raise exceptions.InvalidServer
		except:
			raise exceptions.UnknownError

		if login:
			if result == False:
				raise exceptions.InvalidCredentials
			if self._settings.basedn == None:
				self._settings.basedn = conn.server.info.raw['defaultNamingContext'][0].decode('utf-8') #fix to convert byte to string
			return conn
		return result


	def login(self):
		self._worker = self._authenticate(repr(self._settings.username),repr(self._settings.password),login=True)

	def authenticate(self,username,password):
		return self._authenticate(username,password)
