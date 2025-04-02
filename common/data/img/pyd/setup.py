from distutils.core import setup, Extension


modules = [Extension('num', ['source\\debug\\debug.c', 'source\\num\\num.c'])]


setup(name='pyd', version='1.0', ext_modules=modules)
