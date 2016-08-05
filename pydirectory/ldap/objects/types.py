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
		if len(modlist) > 0:
			self._objects._engine._worker.modify(self.dn.value,modlist)

		if self.cn._is_modified:
			self._objects._engine._worker.modify_dn(self.dn.value,'CN='+self.cn.value)
			self.dn.update('CN='+self.cn.value+','+self.dn.value.split(',')[1:])
			self.cn._is_modified = False

		if self.container._is_modified: #falta por terminar
			self._objects._engine._worker.modify_dn(self.dn.value,'CN='+self.cn.value,new_superior=self.container.value)

			self.container._is_modified = False



		#if self.container._is_modified:
		#	conf = {
		#		"dn": self.dn.value,
		#	}
		#	conf['relative_dn'] = "CN="+self.cn.value

#			if self.container._is_modified:
#				conf['new_superior'] = self.container.value
#			print(conf)
#			if self._objects._engine._worker.modify_dn(**conf):
#				result = True

	def _reset(self):
		obj = self._objects.get(dn=self.dn.value)
		self._attrs = obj._attrs
