import MOKO as Moko
from MOSC import stars

Moko.Stage(stars('*'))
Moko.Stage(stars('NEW SCRIPT'))
Moko.Stage(stars('*'))

language = Moko.Report("language", 'get', 'string', 'string', 'string')

if language == 'English(default)':
    Moko.Stage('*Program*', 'info')
    Moko.Messenger('set', 'Program_info', 'This script implements one of the many functions of Program.')
    Moko.Messenger('set', 'Program', 'The Program function is intended to control various elements from the script '
                                     'MOKO SE programs (scripts, project, control etc). '
                                     'Program has one mode of operation - \'\'set\'\', the function can only write '
                                     'certain commands.')
    Moko.Program('control', 'set', 'save word report')

elif language == 'Русский':
    Moko.Stage('*Program*', 'info')
    Moko.Messenger('set', 'Program_info', 'В этом скрипте реализуется одна из многих функций Program.')
    Moko.Messenger('set', 'Program', 'Функция Program предназначена для управления из скрипта различными элементами программы MOKO SE (scripts, project, control etc). ' +
               'Program имеет один режим работы - \'\'set\'\', т.е. функция может только записывать определенные команды.')
    Moko.Messenger('set', 'Control', 'Сохраняем Word протокол.') 
    Moko.Program('control', 'set', 'save word report')



Moko.Stage(stars('*'))
Moko.Stage(stars('NEXT SCRIPT'))
Moko.Stage(stars('*'))

Moko.EndScript()