from distutils.core import setup, Extension

modules = [Extension('index', ['source\\debug\\debug.c', 'source\\index\\index.c'])]


setup(name='commonPyd', version='1.0', ext_modules=modules)
