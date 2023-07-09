import MOKO

MOKO.Report('Messenger', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')
MOKO.Report('Messenger_clear', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')
MOKO.Report('Messenger_delete', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')

MOKO.Report(f'Messenger', 'set', 'table', '1;2;3;4;5;6;7;8;9')
MOKO.Report(f'Messenger_clear', 'set', 'table', '1;2;3;4;5;6;7;8;9')
MOKO.Report(f'Messenger_delete', 'set', 'table', '1;2;3;4;5;6;7;8;9')
#Region Status (статус)
#hesh Greeting


language = MOKO.Messenger('get', 'Language. Язык.jpg', 'Please select your language in dropdown.\n'
                                                       'Пожалуйста, выберите свой язык в раскрывающемся списке:',
                                                       'choice=English;Русский')

MOKO.Report('language', 'set', 'string', language)
MOKO.Report('language_clear', 'set', 'string', language)
MOKO.Report('language_delete', 'set', 'string', language)


if language == "English":
    MOKO.Messenger('set', 'Greeting.jpg', 'Additional features of Messenger will be shown in the current project.')
elif language == "Русский":
    MOKO.Messenger('set', 'Greeting.jpg', 'В текущем проекте будут показаны дополнительные возможности Messenger.')

MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

MOKO.EndScript()