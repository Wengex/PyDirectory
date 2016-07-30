class Engine(object):
	def __init__(self,settings,autologin=True):
		self._settings = settings
		if autologin:
			self.login()

	def authenticate(self,username,password):
		return False

	def login(self):
		return False
