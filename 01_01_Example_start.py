import MokoRequestsLibrary as Moko
from MokoFormatedLibrary import stars

Moko.Stage(stars('*'))
Moko.Stage(stars('START'))
Moko.Stage(stars('*'))
Moko.Messenger('set', 'Welcome message', 'Dear User!\nThanks for installing MOKO SE.\nEnjoyable using!')
language = Moko.Messenger('get', 'Language', 'Please select your language in dropdown:', 'choice=English (default);Русский;')
Moko.Stage(stars('*'))
Moko.Stage(stars('NEXT SCRIPT'))
Moko.Stage(stars('*'))
Moko.EndScript()