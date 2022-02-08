import MOKO

#Region Status (статус)
#hesh Greeting


language = MOKO.Messenger('get', 'Language. Язык.jpg', 'Please select your language in dropdown.\n'
                                                       'Пожалуйста, выберите свой язык в раскрывающемся списке:',
                                                       'choise = English;Русский')

MOKO.Report('language', 'set', 'string', language)

if language == "English":
    MOKO.Messenger('set', 'Hello.png', 'The current project will show the interaction between MOKO SE and Telegram.')
elif language == "Русский":
    MOKO.Messenger('set', 'Приветствие.png', 'В текущем проекте будет показано взаимодействие MOKO SE и Telegram.')

MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

MOKO.EndScript()