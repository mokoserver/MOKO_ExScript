import MOKO as Moko
from MOSC import stars

Moko.Stage(stars('*'))
Moko.Stage(stars('Новый SCRIPT'))
Moko.Stage(stars('*'))

Moko.Messenger('set', 'Прощание#@bye', 'Предыдущие сообщения продемонстрировали работу Мессенджера. '
                                      'Спасибо что использовали MOKO SE. Приятного пользования!')
Moko.Stage(stars('Конец'))
Moko.Stage(stars('*'))

Moko.EndScript()
