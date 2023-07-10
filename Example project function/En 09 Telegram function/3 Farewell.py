import MOKO
import MTLG

#Region Status
#hesh Farewell

MOKO.Telegram('alpha', 'set', f'********START SCRIPT********')
MTLG.TelegramClassic('alpha', 'set', f'********START SCRIPT********')

alpha = MOKO.Telegram('alpha', 'get', 'list', 'string')
MTLG.TelegramClassic('alpha', 'get', 'list', 'string')

MOKO.Messenger('set', 'Farewell.jpg', 'That\'s all! Good luck!')
MTLG.TelegramMessenger('set', 'Farewell', 'That\'s all! Good luck!')

MOKO.Program('tree', 'set', 'select = ' + 'Farewell')
MTLG.TelegramProgram('tree', 'set', 'select = ' + 'Farewell')
MOKO.Program('tree', 'set', 'chosen = passed')
MTLG.TelegramProgram('tree', 'set', 'chosen = passed')
# EndRegion Status


MOKO.EndScript()
MTLG.TelegramEndScript()

if len(alpha) != 0:
    if language == "English":
        MOKO.Telegram('alpha', 'set', f'********END SCRIPT********')
        MTLG.TelegramClassic('alpha', 'set', f'********END SCRIPT********')