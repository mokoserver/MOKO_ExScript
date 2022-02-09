import MOKO
import MOSC

#Region Status (статус)
#hesh Farewell

MOKO.Telegram('alpha', 'set', f'********START SCRIPT********')
MOSC.TelegramClassic('alpha', 'set', f'********START SCRIPT********')

language = MOKO.Report("language", 'get', 'string', 'string', 'string')
MOSC.TelegramReport("language", 'get', 'string', 'string', 'string')

alpha = MOKO.Telegram('alpha', 'get', 'list', 'string')
MOSC.TelegramClassic('alpha', 'get', 'list', 'string')

if language == 'English':
    MOKO.Messenger('set', 'Farewell.jpg', 'That\'s all! Good luck!')
    MOSC.TelegramMessenger('set', 'Farewell', 'That\'s all! Good luck!')
elif language == 'Русский':
    MOKO.Messenger('set', 'Farewell.jpg', 'На этом всё! Удачи!')
    MOSC.TelegramMessenger('set', 'Farewell', 'На этом всё! Удачи!')

MOKO.Program('tree', 'set', 'select = ' + 'Farewell')
MOSC.TelegramProgram('tree', 'set', 'select = ' + 'Farewell')
MOKO.Program('tree', 'set', 'chosen = passed')
MOSC.TelegramProgram('tree', 'set', 'chosen = passed')
# EndRegion Status


MOKO.EndScript()
MOSC.TelegramEndScript()

if len(alpha) != 0:
    if language == "English":
        MOKO.Telegram('alpha', 'set', f'********END SCRIPT********')
        MOSC.TelegramClassic('alpha', 'set', f'********END SCRIPT********')