import MOKO

MOKO.Messenger('set', 'Приветствие#@hello', 'Дорогой пользователь!\nПрямо сейчас Вам будет продемонстрирована работа '
                                         'плагина Graph.\nПриятного просмотра!')

#Region Status
#hash Greeting
MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status

MOKO.EndScript()