import MOKO

#Region Status (статус)
#hesh Greeting


language = MOKO.Messenger('get', 'Language. Язык.jpg', 'Please select your language in dropdown.\n'
                                                       'Пожалуйста, выберите свой язык в раскрывающемся списке:',
                                                       'choise = English;Русский')

MOKO.Report('language', 'set', 'string', language)
MOKO.Report('language_clear', 'set', 'string', language)
MOKO.Report('language_delete', 'set', 'string', language)


if language == "English":
    MOKO.Messenger('set', 'Greeting.jpg', 'Additional features of Messenger and Report will be shown in the current project.')
elif language == "Русский":
    MOKO.Messenger('set', 'Greeting.jpg', 'В текущем проекте будут показаны дополнительные возможности Messenger и Report.')

MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

MOKO.EndScript()