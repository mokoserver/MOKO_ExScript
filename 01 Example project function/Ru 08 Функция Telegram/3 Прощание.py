import MOKO
import MTLG

#Region Status (статус)
#hesh Farewell

MOKO.Telegram('alpha', 'set', f'********Старт скрипта********')
MTLG.TelegramClassic('alpha', 'set', f'********Старт скрипта********')

alpha = MOKO.Telegram('alpha', 'get', 'list', 'string')
MTLG.TelegramClassic('alpha', 'get', 'list', 'string')

MOKO.Messenger('set', 'Прощание#@bye', 'На этом всё! Удачи!')
MTLG.TelegramMessenger('set', 'Прощание', 'На этом всё! Удачи!')

MOKO.Program('tree', 'set', 'select = ' + 'Farewell')
MTLG.TelegramProgram('tree', 'set', 'select = ' + 'Farewell')
MOKO.Program('tree', 'set', 'chosen = passed')
MTLG.TelegramProgram('tree', 'set', 'chosen = passed')
# EndRegion Status


MOKO.EndScript()
MTLG.TelegramEndScript()

if len(alpha) != 0:
    MOKO.Telegram('alpha', 'set', f'********Конец скрипта********')
    MTLG.TelegramClassic('alpha', 'set', f'********Конец скрипта********')