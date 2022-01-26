import MOKO as Moko
from MOSC import stars

Moko.Stage(stars('*'))
Moko.Stage(stars('START'))
Moko.Stage(stars('*'))
language = Moko.Messenger('get', 'Language. Язык.jpg', 'Please select your language in dropdown.\nПожалуйста, выберите свой язык в раскрывающемся списке:',
                          'choice=English(default);Русский;')
Moko.Report("language", 'set', 'string', language)
if language == 'English(default)':
    Moko.Messenger('set', 'Greeting.jpg', 'Dear User!\nThanks for installing MOKO SE.\nEnjoyable using!')
elif language == 'Русский':
    Moko.Messenger('set', 'Greeting.jpg', 'Дорогой пользователь!\nСпасибо, что установили MOKO SE.\nПриятного пользования!')
Moko.Stage(stars('*'))
Moko.Stage(stars('NEXT SCRIPT'))
Moko.Stage(stars('*'))
Moko.EndScript()