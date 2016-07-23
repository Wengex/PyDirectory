from ldap.ldap import Settings as SettingsLdap

class Tools(object):
	def setQuery():
		pass

class Settings(dict):
	def __init__(self,type,*args,**kwargs):
		if type == 'ldap':
			settings = SettingsLdap(**kwargs)

		for key,value in settings():
			self[key] = value
			setattr(self,key,value)

		self.engine = settings.engine

		super(Settings,self).__init__(*args,**kwargs)
