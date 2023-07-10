import MOKO as Moko
from MOSC import stars

Moko.Stage(stars('*'))
Moko.Stage(stars('Новый SCRIPT'))
Moko.Stage(stars('*'))

Moko.Stage('*Program*', 'info')
Moko.Messenger('set', 'Program_info', 'В этом скрипте реализуется одна из многих функций Program.')
Moko.Messenger('set', 'Program', 'Функция Program предназначена для управления из скрипта различными элементами '
                                 'программы MOKO SE (scripts, project, control etc). ' +
                                 'Program имеет один режим работы - \'\'set\'\', т.е. '
                                 'функция может только записывать определенные команды.')

Moko.Messenger('set', 'Control', 'Сохраняем Word протокол.')
Moko.Program('control', 'set', 'save word report')

Moko.Stage(stars('*'))
Moko.Stage(stars('Следующий SCRIPT'))
Moko.Stage(stars('*'))

Moko.EndScript()
