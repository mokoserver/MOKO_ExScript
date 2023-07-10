import MOKO
import MTLG

MOKO.Telegram('alpha', 'set', f'********START SCRIPT********')
MTLG.TelegramClassic('alpha', 'set', f'********START SCRIPT********')

#Region Status
#hesh Using Telegram

text = ''
id = ''

alpha = MOKO.Telegram('alpha', 'get', 'list', 'string')
MTLG.TelegramClassic('alpha', 'get', 'list', 'string')

if len(alpha) == 0:
    MOKO.Messenger('set', 'Telegram.png', 'Please, find the MOKO SE BOT (@MokoSeBot) in Telegram. '
                                          'Then run it and write the following message:\'\'. '
                                          'After that follow the instructions!')
    MTLG.TelegramMessenger('set', 'Telegram', 'Please, find the MOKO SE BOT (@MokoSeBot) in Telegram. '
                                              'Then run it and write the following message: \'\'. '
                                              'After that follow the instructions!')
else:
    text = MOKO.Messenger('get', 'Telegram.png', 'Please, enter text.', 'string')
    MTLG.TelegramMessenger('get', 'Telegram', 'Please, enter text.', 'string')
    if text == '':
        text = "Hello, I'm a MOKO SE BOT!"

    MOKO.Telegram('alpha', 'set', f'{text}')
    MTLG.TelegramClassic('alpha', 'set', f'{text}')

MOKO.Program('tree', 'set', 'select = ' + 'Using Telegram')
MTLG.TelegramProgram('tree', 'set', 'select = ' + 'Using Telegram')
MOKO.Program('tree', 'set', 'chosen = passed')
MTLG.TelegramProgram('tree', 'set', 'chosen = passed')


MOKO.EndScript()
MTLG.TelegramEndScript()

if len(alpha) != 0:
    MOKO.Telegram('alpha', 'set', f'********END SCRIPT********')
    MTLG.TelegramClassic('alpha', 'set', f'********END SCRIPT********')