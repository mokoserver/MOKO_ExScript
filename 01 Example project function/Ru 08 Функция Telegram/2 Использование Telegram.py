import MOKO
import MTLG

#scriptname = MOSC.ScriptName()
#scriptname = scriptname[0:-3] # delete 3 elements at the end of the string

MOKO.Telegram('alpha', 'set', f'********Старт скрипта********')
MTLG.TelegramClassic('alpha', 'set', f'********Старт скрипта********')

#MOKO.Telegram('alpha', 'set', f'***{scriptname}***')

#Region Status (статус)
#hesh Using Telegram

text = ''
id = ''

alpha = MOKO.Telegram('alpha', 'get', 'list', 'string')
MTLG.TelegramClassic('alpha', 'get', 'list', 'string')

if len(alpha) == 0:
    MOKO.Messenger('set', 'Telegram.png', 'Пожалуйста, найдите MOKO SE BOT (@MokoSeBot) в Telegram. '
                                          'Затем запустите его и напишите следующее сообщение: \'\'Как подключить тебя к MOKO SE?\'\'. '
                                          'После этого следуйте инструкциям!')
    MTLG.TelegramMessenger('set', 'Telegram', 'Пожалуйста, найдите MOKO SE BOT (@MokoSeBot) в Telegram. '
                                          'Затем запустите его и напишите следующее сообщение: \'\'Как подключить тебя к MOKO SE?\'\'. '
                                          'После этого следуйте инструкциям!')
else:
    text = MOKO.Messenger('get', 'Telegram.png', 'Пожалуйста, введите текст.', 'string')
    MTLG.TelegramMessenger('get', 'Telegram', 'Пожалуйста, введите текст.', 'string')
    if text == '':
        text = "Привет, я MOKO SE BOT!"

    MOKO.Telegram('alpha', 'set', f'{text}')
    MTLG.TelegramClassic('alpha', 'set', f'{text}')

MOKO.Program('tree', 'set', 'select = ' + 'Using Telegram')
MTLG.TelegramProgram('tree', 'set', 'select = ' + 'Using Telegram')
MOKO.Program('tree', 'set', 'chosen = passed')
MTLG.TelegramProgram('tree', 'set', 'chosen = passed')


MOKO.EndScript()
MTLG.TelegramEndScript()

if len(alpha) != 0:
    MOKO.Telegram('alpha', 'set', f'********Конец скрипта********')
    MTLG.TelegramClassic('alpha', 'set', f'********Конец скрипта********')