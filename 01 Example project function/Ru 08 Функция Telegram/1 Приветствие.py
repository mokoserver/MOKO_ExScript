import MOKO
import MTLG

#MOKO.Telegram('alpha', 'set', f'{stars("*")}')
#MOKO.Telegram('alpha', 'set', 'START')
#MOKO.Telegram('alpha', 'set', f'{stars("*")}')

#scriptname = MOSC.ScriptName()
MOKO.Telegram('alpha', 'set', f'********Старт скрипта********')
MTLG.TelegramClassic('alpha', 'set', f'********Старт скрипта********')
#MOKO.Telegram('alpha', 'set', f'***{scriptname}***')

#Region Status (статус)
#hash Greeting

alpha = MOKO.Telegram('alpha', 'get', 'list', 'string')

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
    MOKO.Telegram('alpha', 'set', f'********Конец скрипта********')
    MTLG.TelegramClassic('alpha', 'set', f'********Конец скрипта********')
