from directory.objects import types
from ldap3 import MODIFY_DELETE

class object(types.object):
	def save(self):
		modlist = {}
		for key,attr in self._attrs.items():
			if attr._is_modified and (not attr._is_rdn):
				operator = attr._operator
				modlist[key]= [(operator,attr.raw)]
				attr._is_modified = False
		for key in self._drops:
			operator = MODIFY_DELETE
			modlist[key] = [(operator,[])]
		self._drops = []
		if len(modlist) <= 0:
			return False
		if self._objects._engine._worker.modify(self.dn.value,modlist):
			return True
		return False

	def _reset(self):
		obj = self._objects.get(dn=self.dn.value)
		self._attrs = obj._attrs
