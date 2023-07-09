import MOKO
import MTLG

#MOKO.Telegram('alpha', 'set', f'{stars("*")}')
#MOKO.Telegram('alpha', 'set', 'START')
#MOKO.Telegram('alpha', 'set', f'{stars("*")}')

#scriptname = MOSC.ScriptName()
MOKO.Telegram('alpha', 'set', f'********START SCRIPT********')
MTLG.TelegramClassic('alpha', 'set', f'********START SCRIPT********')
#MOKO.Telegram('alpha', 'set', f'***{scriptname}***')

#Region Status (статус)
#hesh Greeting


language = MOKO.Messenger('get', 'Language. Язык.jpg', 'Please select your language in dropdown.\n'
                                                       'Пожалуйста, выберите свой язык в раскрывающемся списке:',
                                                       'choise = English;Русский')

MTLG.TelegramMessenger('get', 'Language. Язык', 'Please select your language in dropdown.\n'
                                                       'Пожалуйста, выберите свой язык в раскрывающемся списке:',
                                                       'choise = English;Русский')

alpha = MOKO.Telegram('alpha', 'get', 'list', 'string')
MTLG.TelegramClassic('alpha', 'get', 'list', 'string')
MTLG.TelegramDriver('alpha', 'get', 'list', 'string')

#if len(alpha) != 0:
#    if language == "English":
#        MOKO.Telegram('alpha', 'set', f'***Selected language - {language}***')
#    elif language == "Русский":
#        MOKO.Telegram('alpha', 'set', f'***Выбранный язык - {language}***')

MOKO.Report('language', 'set', 'string', language)
MTLG.TelegramReport('language', 'set', 'string', language)


if language == "English":
    if len(alpha) != 0:
        MTLG.TelegramMessenger('set', 'Hello', 'The current project will show the interaction between MOKO SE and Telegram.')
    MOKO.Messenger('set', 'Hello.png', 'The current project will show the interaction between MOKO SE and Telegram.')

elif language == "Русский":
    if len(alpha) != 0:
        MTLG.TelegramMessenger('set', 'Приветствие', 'В текущем проекте будет показано взаимодействие MOKO SE и Telegram.')
    MOKO.Messenger('set', 'Приветствие.png', 'В текущем проекте будет показано взаимодействие MOKO SE и Telegram.')


MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MTLG.TelegramProgram('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
MTLG.TelegramProgram('tree', 'set', 'chosen = passed')
# EndRegion Status

MOKO.EndScript()
MTLG.TelegramEndScript()

if len(alpha) != 0:
    MOKO.Telegram('alpha', 'set', f'********END SCRIPT********')
    MTLG.TelegramClassic('alpha', 'set', f'********END SCRIPT********')
