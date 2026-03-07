import MOKO
from MOSC import stars

MOKO.Stage(stars('*'))
MOKO.Stage(stars('MOKO Clicker'))
MOKO.Stage(stars('*'))

MOKO.Messenger('set', 'Приветствие#@hello', 'В данном презентации будут показаны 3 команды, но команд больше. '
                                         'Первая команда - получение скриншота экрана, '
                                         'вторая команда - указание пути картинки, '
                                         'последняя команда - получение картинки по указанному пути.')

#Region Status (статус)
#hash Greeting
MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status

MOKO.EndScript()
