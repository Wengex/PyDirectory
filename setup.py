from distutils.core import setup

requires = []

try:
	import ldap
except:
	requires.append('python-ldap')

setup(
	name="pydirectory",
	version="0.0.0",
	description="Python frameWork to managing multiples LDAP services",
	author="Jonas Delgado Mesa",
	author_email="jdelgado@yohnah.net",
	url="https://github.com/Wengex/PyDirectory",
	license="GPLv2",
	packages=["pydirectory"],
	long_description=open('README.txt').read(),
	install_requires = requires
)
