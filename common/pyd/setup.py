from distutils.core import setup, Extension

modules = [Extension('createPass', ['source\\debug\\debug.c', 'source\\pass\\createPass.c']),
           Extension('hitJudge', ['source\\debug\\debug.c', 'source\\hit\\hit.c']),
           Extension('status', ['source\\debug\\debug.c', 'source\\status\\status.c']),
           Extension('save', ['source\\debug\\debug.c', 'source\\save\\save.c']),
           Extension('calc', ['source\\debug\\debug.c', 'source\\calc\\calc.c']),
           Extension('key', ['source\\debug\\debug.c', 'source\\key\\key.c'])]


setup(name='commonPyd', version='1.0', ext_modules=modules)
