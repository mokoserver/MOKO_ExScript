import MOKO as Moko
from MOSC import stars

Moko.Stage(stars('*'))
Moko.Stage(stars('NEW SCRIPT'))
Moko.Stage(stars('*'))
language = Moko.Report("language", 'get', 'string', 'string', 'string')
if language == 'English(default)':
   Moko.Messenger('set', 'Farewell.jpg', 'Previous messages demonstrated the work of the Messenger. Thanks for using MOKO SE. Good luck!')
   Moko.Stage(stars('*'))
   Moko.Stage(stars('END'))
   Moko.Stage(stars('*'))
elif language == 'Русский':
   Moko.Messenger('set', 'Farewell.jpg', 'Предыдущие сообщения продемонстрировали работу Мессенджера. Спасибо что использовали MOKO SE. Приятного пользования!')
   Moko.Stage(stars('Конец'))
   Moko.Stage(stars('*'))
Moko.EndScript()
