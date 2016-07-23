from socket import gethostbyname, gaierror
import exceptions
import getpass

class Settings(object):
	def __init__(self):
		self.opt = {}

	def __call__(self):
		try:
			self.opt['host'] = gethostbyname(self.opt['hostname'])
		except gaierror:
			raise exceptions.InvalidServer
		self.engine = self.opt['engine']()
		self.engine.settings = self.opt
		return self.opt.items()
