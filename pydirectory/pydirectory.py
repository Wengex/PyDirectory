import importlib


class Directory(object):
	def __init__(self,type,autologin=True,**kwargs):
		self.settings = importlib.import_module("%(type)s.settings" % {'type':type}).settings(**kwargs)
		self.engine = importlib.import_module("%(type)s.engine" % {'type':type}).engine(self.settings,autologin)
		self.objects = importlib.import_module("%(type)s.objects" % {'type':type}).objects(self.engine)
