from directory.objects import types


class object(types.object):
	def save(self):
		modlist = {}
		for key,attr in self._attrs.items():
			if attr._is_modified and (not attr._use_rdn):
				modlist[key]= [(attr._operator,attr.raw)]
		if self._engine._worker.modify(self.dn.value,modlist):
			return True
		return False
