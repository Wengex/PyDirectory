from directory.settings import Settings, Option
from directory.classes import Engine, Actions, Objects


class settings(Settings):
	def options(self):
		self.hostname = Option(null=False,type=str)
		self.username = Option(null=True)
		self.password = Option(null=True)

class engine (Engine):
	def __init__(self,**settings):
		pass


class actions (Actions):
	def __init__(self,**kwargs):
		pass

	def authentication(self):
		pass


class objects(object):
	pass
