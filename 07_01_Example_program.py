import MokoRequestLib as Moko
from MokoFormatedLibrary import stars

Moko.Stage(stars('*'))
Moko.Stage(stars('NEW SCRIPT'))
Moko.Stage(stars('*'))

language = Moko.Report("language", 'get', 'string', 'string')

if language == 'English(default)':
    Moko.Stage('*Program*', 'info')
    Moko.Messenger('set', 'Program_info', 'This script implements one of the many functions of Program.')
    Moko.Messenger('set', 'Program', 'The Program function is intended to control various elements from the script '
                                     'MOKO SE programs (scripts, project, control etc). '
                                     'Program has one mode of operation - *set*, the function can only write '
                                     'certain commands.')
    Moko.Messenger('set', 'Control', 'We implement saving the word protocol at the request of the user through control.'
                                     ' Clicking on * Yes * in the next message will open the word log of the '
                                     'entire project however, the script will continue to execute. '
                                     'Accordingly, when you click on * No *, the protocol will not open and'
                                     'the project will continue to run as well.')
    a = Moko.Messenger('get', 'Report', 'Do you want to print word report?', 'boolean')
    if a == True:
        Moko.Program('control', 'set', 'save word report')

elif language == 'Русский':
    Moko.Stage('*Program*', 'info')
    Moko.Messenger('set', 'Program_info', 'В этом скрипте реализуется одна из многих функций Program.')
    Moko.Messenger('set', 'Program', 'Функция Program предназначена для управления из скрипта различными элементами '
                                     'программы MOKO SE (scripts, project, control etc). ' 
                                     'Program имеет один режим работы - *set*, т.е. функция может '
                                     'только записывать определенные команды.')
    Moko.Messenger('set', 'Control', 'Реализуем сохранение word протокола по желанию пользователя через control. ' 
                                     'При нажатии на *Yes* в следующем сообщении откроется word протокол всего проекта,'
                                     ' однако скрипт будет выполняться далее. ' 
                                     'Соответсвенно, при нажатии на *No* протокол не '
                                     'откроется и проект так же продолжит выполняться.')
    a = Moko.Messenger('get', 'Report', 'Хотите напечатать word протокол??', 'boolean')
    if a == True:
        Moko.Program('control', 'set', 'save word report')


Moko.Stage(stars('*'))
Moko.Stage(stars('NEXT SCRIPT'))
Moko.Stage(stars('*'))

Moko.EndScript()