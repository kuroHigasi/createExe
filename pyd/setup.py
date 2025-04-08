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
           Extension('indexSave', ['source\\indexSave\\index.c']),
           Extension('indexDungeon', ['source\\dungeon\\indexDungeon\\index.c']),
           Extension('way', ['source\\dungeon\\way\\way.c']),
           Extension('typeAction', ['source\\dungeon\\typeAction\\action.c']),
           Extension('typeEnemy', ['source\\dungeon\\typeEnemy\\enemyType.c']),
           Extension('typeEvent', ['source\\dungeon\\typeEvent\\eventType.c']),
           Extension('typeItem', ['source\\dungeon\\typeItem\\itemType.c']),
           Extension('mask', ['source\\dungeon\\mask\\mask.c'])]


setup(name='commonPyd', version='1.0', ext_modules=modules)
