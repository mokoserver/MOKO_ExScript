import MOKO
import MOSC

#scriptname = MOSC.ScriptName()
#scriptname = scriptname[0:-3] # delete 3 elements at the end of the string

MOKO.Telegram('alpha', 'set', f'********START SCRIPT********')
MOSC.TelegramClassic('alpha', 'set', f'********START SCRIPT********')

language = MOKO.Report("language", 'get', 'string', 'string', 'string')
MOSC.TelegramReport("language", 'get', 'string', 'string', 'string')

#MOKO.Telegram('alpha', 'set', f'***{scriptname}***')

#Region Status (статус)
#hesh Using Telegram

text = ''
id = ''

alpha = MOKO.Telegram('alpha', 'get', 'list', 'string')
MOSC.TelegramClassic('alpha', 'get', 'list', 'string')

if len(alpha) == 0:
    if language == "English":
        MOKO.Messenger('set', 'Telegram.png', 'Please, find the MOKO SE BOT (@MokoSeBot) in Telegram. '
                                              'Then run it and write the following message: \'\'Как подключить тебя к MOKO SE?\'\'. '
                                              'After that follow the instructions!')
        MOSC.TelegramMessenger('set', 'Telegram', 'Please, find the MOKO SE BOT (@MokoSeBot) in Telegram. '
                                              'Then run it and write the following message: \'\'Как подключить тебя к MOKO SE?\'\'. '
                                              'After that follow the instructions!')
    elif language == "Русский":
        MOKO.Messenger('set', 'Telegram.png', 'Пожалуйста, найдите MOKO SE BOT (@MokoSeBot) в Telegram. '
                                              'Затем запустите его и напишите следующее сообщение: \'\'Как подключить тебя к MOKO SE?\'\'. '
                                              'После этого следуйте инструкциям!')
        MOSC.TelegramMessenger('set', 'Telegram', 'Пожалуйста, найдите MOKO SE BOT (@MokoSeBot) в Telegram. '
                                              'Затем запустите его и напишите следующее сообщение: \'\'Как подключить тебя к MOKO SE?\'\'. '
                                              'После этого следуйте инструкциям!')
else:
    if language == "English":
        text = MOKO.Messenger('get', 'Telegram.png', 'Please, enter text.', 'string')
        MOSC.TelegramMessenger('get', 'Telegram', 'Please, enter text.', 'string')
        if text == '':
            text = "Hello, I'm a MOKO SE BOT!"
    elif language == "Русский":
        text = MOKO.Messenger('get', 'Telegram.png', 'Пожалуйста, введите текст.', 'string')
        MOSC.TelegramMessenger('get', 'Telegram', 'Пожалуйста, введите текст.', 'string')
        if text == '':
            text = "Привет, я MOKO SE BOT!"

    MOKO.Telegram('alpha', 'set', f'{text}')
    MOSC.TelegramClassic('alpha', 'set', f'{text}')

MOKO.Program('tree', 'set', 'select = ' + 'Using Telegram')
MOSC.TelegramProgram('tree', 'set', 'select = ' + 'Using Telegram')
MOKO.Program('tree', 'set', 'chosen = passed')
MOSC.TelegramProgram('tree', 'set', 'chosen = passed')


MOKO.EndScript()
MOSC.TelegramEndScript()

if len(alpha) != 0:
    if language == "English":
        MOKO.Telegram('alpha', 'set', f'********END SCRIPT********')
        MOSC.TelegramClassic('alpha', 'set', f'********END SCRIPT********')