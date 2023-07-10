import MOKO

#Region Status (статус)
#hesh Greeting

language = MOKO.Messenger('get', 'Language.jpg', 'Please select your language in dropdown.\n'
                                                       'Пожалуйста, выберите свой язык в раскрывающемся списке:',
                                                       'choise = English;Русский;')

MOKO.Report('language', 'set', 'string', language)

if language == "English":
    MOKO.Messenger('set', 'Greeting.jpg', 'The current project will show the plugin\'s control options. '
                                          'In this example, everything will be shown based on the Graph plugin.')
elif language == "Русский":
    MOKO.Messenger('set', 'Greeting.jpg', 'В текущем проекте будут показаны возможности управления плагином. '
                                          'В данном примере всё будет показываться на основе плагина Graph.')

MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

MOKO.EndScript()