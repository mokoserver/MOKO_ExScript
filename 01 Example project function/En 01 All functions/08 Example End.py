import MOKO as Moko
from MOSC import stars

Moko.Stage(stars('*'))
Moko.Stage(stars('NEW SCRIPT'))
Moko.Stage(stars('*'))

Moko.Messenger('set', 'Farewell.jpg', 'Previous messages demonstrated the work of the Messenger. '
                                      'Thanks for using MOKO SE. Good luck!')
Moko.Stage(stars('*'))
Moko.Stage(stars('END'))
Moko.Stage(stars('*'))

Moko.EndScript()
