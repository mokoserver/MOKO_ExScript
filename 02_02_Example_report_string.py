import MokoRequestLib as Moko
from MokoFormatedLibrary import stars, choice_language


Moko.Stage(stars('*'))
Moko.Stage(stars('NEW SCRIPT'))
Moko.Stage(stars('*'))

language = Moko.Report("language", 'get', 'string', 'string')

if language == 'English(default)':
    Moko.Messenger('set', 'Script message',
                   'In the current script in the test protocol, data is written as a string according to certain bookmarks.')
    Moko.Messenger('set', 'Report mode',
                   'The Report function has 2 types: *set* and *get*. To write any data to the protocol, use the *set* type'
                    'The *get* type is used when getting data from the protocol.')
    Moko.Messenger('set', 'Report name',
                   'Report name is a function parameter that specifies the name of a bookmark defined in the Word-protocol.')
    Moko.Messenger('set', 'Report kind',
                   'Report kind is a parameter that defines in what form data is written to the protocol (*string*, *table*).')
    Moko.Report("string1", 'set', 'string', 'Test table 1')
    Moko.Report("string2", 'set', 'string', 'Test table 2')

elif language == 'Русский':
    Moko.Messenger('set', 'Script message',
                       'В текущем скрипте в тестовом протоколе данные записываются в виде строки по определенным закладкам.')
    Moko.Messenger('set', 'Report mode',
                       'Функция Report имеет 2 типа: *set* и *get*. Для записи каких-либо данных в протокол используется тип *set*'
                       'Тип *get* используется в случае получения данных из протокола.')
    Moko.Messenger('set', 'Report name',
                       'Report name - параметр функции, в котором задаётся название закладки, определённой в Word-протоколе.')
    Moko.Messenger('set', 'Report kind',
                       'Report kind - параметр, определяющий в каком виде записывать данные в протокол (*string*, *table*).')
    Moko.Report("string1", 'set', 'string', 'Тестовая таблица 1')
    Moko.Report("string2", 'set', 'string', 'Тестовая таблица 2')

Moko.Stage(stars('*'))
Moko.Stage(stars('NEXT SCRIPT'))
Moko.Stage(stars('*'))
Moko.EndScript()