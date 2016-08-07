import importlib


class Directory(object):
	def __init__(self,type,autologin=True,**kwargs):
		self.settings = importlib.import_module("%(type)s.settings.classes" % {'type':type}).settings(type,**kwargs)
		self.engine = importlib.import_module("%(type)s.engine.classes" % {'type':type}).engine(self.settings,autologin)
		self.objects = importlib.import_module("%(type)s.objects.classes" % {'type':type}).objects(self.engine)
		self.tools = importlib.import_module("%(type)s.tools" % {'type':type}).tools(type)
