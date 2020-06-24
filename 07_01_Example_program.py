import MokoRequestsLibrary as Moko
from MokoFormatedLibrary import stars

Moko.Stage(stars('*'))
Moko.Stage(stars('NEW SCRIPT'))
Moko.Stage(stars('*'))

Moko.Stage('*Program*', 'info')
Moko.Messenger('set', 'Program_info', 'В этом скрипте реализуется одна из многих функций Program.')
Moko.Messenger('set', 'Program', 'Функция Program предназначена для управления из скрипта различными элементами программы MOKO SE (scripts, project, control etc). ' +
               'Program имеет один режим работы - *set*, т.е. функция может только записывать определенные команды.')
Moko.Messenger('set', 'Control', 'Реализуем сохранение word протокола по желанию пользователя через control. ' +
               'При нажатии на *Yes* в следующем сообщении откроется word протокол всего проекта, однако скрипт будет выполняться далее. ' +
               'Соответсвенно, при нажатии на *No* протокол не откроется и проект так же продолжит выполняться.')
a = Moko.Messenger('get', 'Report', 'Печатать word протокол?', 'boolean')
if a == True:
    Moko.Program('control', 'set', 'save word report')

Moko.Stage(stars('*'))
Moko.Stage(stars('NEXT SCRIPT'))
Moko.Stage(stars('*'))

Moko.EndScript()