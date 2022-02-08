import MOKO

language = MOKO.Report("language", 'get', 'string', 'string', 'string')

#Region Status (статус)
#hesh Using Telegram

def ParseStringIntoArray(string):
    array = string.split(';')
    return array

text = ''
id = ''

alpha = MOKO.Telegram('alpha', 'get', 'list')



if language == "English":
    id = MOKO.Messenger('get', 'Telegram.png', 'Please, enter your Telegram ID.', 'string')
    text = MOKO.Messenger('get', 'Telegram.png', 'Please, enter text.', 'string')
    if text == '':
        text = "Hello, I'm a MOKO SE BOT!"

elif language == "Русский":
    id = MOKO.Messenger('get', 'Telegram.png', 'Пожалуйста, введите свой Telegram ID.', 'string')
    text = MOKO.Messenger('get', 'Telegram.png', 'Пожалуйста, введите текст.', 'string')
    if text == '':
        text = "Привет, я MOKO SE BOT!"

if id == '':
    MOKO.Telegram('alpha', 'set', f'{text}')
else:
    MOKO.Telegram(f'{id}', 'set', f'{text}')

MOKO.Program('tree', 'set', 'select = ' + 'Using Telegram')
MOKO.Program('tree', 'set', 'chosen = passed')


MOKO.EndScript()