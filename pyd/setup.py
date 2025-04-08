from distutils.core import setup, Extension

modules = [Extension('createPass', ['source\\pass\\createPass.c']),
           Extension('hitJudge', ['source\\hit\\hit.c']),
           Extension('status', ['source\\status\\status.c']),
           Extension('save', ['source\\save\\save.c']),
           Extension('calc', ['source\\calc\\calc.c']),
           Extension('indexHome', ['source\\indexHome\\index.c']),
           Extension('indexConfig', ['source\\indexConfig\\index.c']),
           Extension('indexEnd', ['source\\indexEnd\\index.c']),
           Extension('imgNum', ['source\\imgNum\\num.c']),
           Extension('indexSave', ['source\\indexSave\\index.c'])]


setup(name='commonPyd', version='1.0', ext_modules=modules)
