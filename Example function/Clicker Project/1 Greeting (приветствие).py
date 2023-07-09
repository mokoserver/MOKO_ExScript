import MOKO
from MOSC import stars

MOKO.Stage(stars('*'))
MOKO.Stage(stars('MOKO Clicker'))
MOKO.Stage(stars('*'))

language = MOKO.Messenger('get', 'Language. Язык.jpg', 'Please select your language in dropdown.\nПожалуйста, выберите свой язык в раскрывающемся списке:',
                          'choice=English;Русский;')
MOKO.Report("language", 'set', 'string', language)

#Region Choice language (выбор языка)
#hesh Language
MOKO.Program('tree', 'set', 'select = ' + 'Language')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Choice language

if language == 'English':
    MOKO.Messenger('set', 'Greeting.jpg',
                   'This presentation will show 3 commands, but there are more commands. '
                   'The first command is to get a screenshot of the screen, '
                   'the second command is to specify the image path and '
                   'the last command is to get the image from the specified path.')
elif language == 'Русский':
    MOKO.Messenger('set', 'Greeting.jpg',
                   'В данном презентации будут показаны 3 команды, но команд больше. '
                   'Первая команда - получение скриншота экрана, '
                   'вторая команда - указание пути картинки, '
                   'последняя команда - получение картинки по указанному пути.')


#Region Status (статус)
#hesh Greeting
MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status

MOKO.EndScript()