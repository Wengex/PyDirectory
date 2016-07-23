from ldap3 import Server, Connection, ALL, SUBTREE, BASE
from libs.settings import Settings as SettingsBase
from libs.objects import ObjectList
import exceptions

class Settings(SettingsBase):
	def __init__(self,dc,username,password,baseDN=None,port=None,ssl=False):
		super(Settings,self).__init__()
		self.opt['hostname'] = dc
		self.opt['dc'] = dc
		self.opt['username'] = username
		self.opt['password'] = password
		self.opt['baseDN'] = baseDN
		self.opt['ssl'] = ssl
		if port != None:
			self.opt['port'] = port
		self.opt['engine'] = LDAP





class LDAP(object):
	class Methods(object):
		def __init__(self,settings):
			self.settings = settings
			server_options = {
				"host" : settings['host'],
				"use_ssl" : settings['ssl'],
				"get_info" : ALL
			}
			if settings.get('port',False):
				server_options['port'] = settings["port"]
			self.server = Server(**server_options)
			if not self.authentication(settings['username'],settings['password'],login=True):
				raise exceptions.InvalidCredentials
			if self.settings.get('baseDN',None) == None:
				self.settings['baseDN'] = self.server.info.raw['defaultNamingContext'][0]

		def authentication(self,username,password,login=False):
			conn = Connection(self.server, user=username,password=password)
			result = False
			try:
				result = conn.bind()
			except ldap3.LDAPSocketOpenError:
				raise exceptions.InvalidServer
			except:
				raise exceptions.UnknownError

			if login and result:
				self.worker = conn
			return result



		def search(self,query,attributes=['*'],baseDN=None,scope='subtree'):
			attributes.append('+')
			if scope.lower() == 'subtree':
				searchScope = SUBTREE
			elif scope.lower() == 'base':
				searchScope = BASE
			else:
				raise exceptions.AttributeNotValid('Scope attribute value is not valid. Only subtree or base must be use')
			if baseDN == None:
				basedn = self.settings['baseDN']
			result = ObjectList()
			c = self.worker
			c.search(search_base = basedn,search_filter = query, search_scope = SUBTREE, attributes = attributes, paged_size = 1000)
			for entry in c.response:
				result.append(entry)
				cookie = c.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
			while cookie:
				c.search(search_base = basedn,search_filter = query,search_scope = SUBTREE,attributes = attributes,paged_size = 1000,paged_cookie = cookie)
				cookie = c.result['controls']['1.2.840.113556.1.4.319']['value']['cookie']
				for entry in c.response:
					result.append(entry)
			return result


	def __call__(self):
		return self.Methods(self.settings)
		#self.server = Server(host=self.settings['host'], use_ssl=True, get_info=ALL)
