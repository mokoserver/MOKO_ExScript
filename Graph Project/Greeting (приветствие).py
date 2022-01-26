import MOKO

language = MOKO.Messenger('get', 'Language. Язык.', 'Please select your language in dropdown.\n'
                                                    'Пожалуйста, выберите свой язык в раскрывающемся списке:',
                                                    'choice=English;Русский;')
MOKO.Messenger('set', '1 logo moko.jpg', 'Please select your language in dropdown.\n'
                                                'Пожалуйста, выберите свой язык в раскрывающемся списке:',
                                                'choice=English;Русский;')
MOKO.Report("language", 'set', 'string', language)
if language == 'English':
    MOKO.Messenger('set', 'Welcome message', 'Dear user! Right now, the work of the Graph plugin will be demonstrated to you. '
                                             'Happy viewing!')
elif language == 'Русский':
    MOKO.Messenger('set', 'Приветствие', 'Дорогой пользователь!\nПрямо сейчас Вам будет продемонстрирована работа плагина Graph.\n'
                                         'Приятного просмотра!')

#Region Status
#hesh Greeting
MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status

MOKO.EndScript()