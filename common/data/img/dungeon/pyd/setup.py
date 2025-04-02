from distutils.core import setup, Extension

modules = [Extension('index', ['source\\debug\\debug.c', 'source\\index\\index.c']),
           Extension('way', ['source\\debug\\debug.c', 'source\\way\\way.c']),
           Extension('action', ['source\\debug\\debug.c', 'source\\action\\action.c']),
           Extension('enemyType', ['source\\debug\\debug.c', 'source\\enemyType\\enemyType.c']),
           Extension('eventType', ['source\\debug\\debug.c', 'source\\eventType\\eventType.c']),
           Extension('itemType', ['source\\debug\\debug.c', 'source\\itemType\\itemType.c']),
           Extension('mask', ['source\\debug\\debug.c', 'source\\mask\\mask.c'])]


setup(name='pyd', version='1.0', ext_modules=modules)
