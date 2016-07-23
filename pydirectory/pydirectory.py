

#from ldap.ldap import LDAP
#from utils import Tools, Settings

import importlib


class Directory(object):
	def __init__(self,type,**kwargs):
		self.settings = importlib.import_module("%(type)s.classes" % {'type':type}).settings(**kwargs)
		self.engine = importlib.import_module("%(type)s.classes" % {'type':type}).engine()
		self.actions = importlib.import_module("%(type)s.classes" % {'type':type}).actions()


#class bakDirectory (object):
#	def __init__(self,**kwargs):

#		settings = Settings(**kwargs)

#		self.engine = settings.engine()

#	def __del__(self):
#		pass


#	def authentication(self,username,password):
#		pass
#

#	@property
#	def get(self):
#		pass

#	@property
#	def search(self):
#		pass
