import MOKO as Moko
from MOSC import stars

Moko.Stage(stars('*'))
Moko.Stage(stars('START'))
Moko.Stage(stars('*'))

Moko.Messenger('set', 'Greeting#@hello', 'Dear User!\nThanks for installing MOKO SE.\nEnjoyable using!')

Moko.Stage(stars('*'))
Moko.Stage(stars('NEXT SCRIPT'))
Moko.Stage(stars('*'))
Moko.EndScript()