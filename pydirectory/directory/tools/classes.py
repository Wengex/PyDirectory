import importlib
class tools(object):
	def __init__(self,type):
		actions = importlib.import_module("%(type)s.tools.actions" % {'type':type})
		for action in dir(actions):
			if action.find('_') != 0:
				try:
					obj = getattr(actions,action)()
					setattr(self,action,obj)
				except TypeError:
					pass
