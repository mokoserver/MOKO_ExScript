import MOKO
import MTLG


MOKO.Telegram('alpha', 'set', f'********START SCRIPT********')
MTLG.TelegramClassic('alpha', 'set', f'********START SCRIPT********')

#Region Status
#hesh Greeting


alpha = MOKO.Telegram('alpha', 'get', 'list', 'string')


if len(alpha) != 0:
    MTLG.TelegramMessenger('set', 'Hello', 'The current project will show the interaction between MOKO SE and Telegram.')
MOKO.Messenger('set', 'Hello#@hello', 'The current project will show the interaction between MOKO SE and Telegram.')

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
