import MOKO
from MOSC import stars

MOKO.StageSeparator()
MOKO.StageSeparator('START')
MOKO.StageSeparator()

MOKO.MessageSetWithImage('Greeting',
                         'Dear User!\nThanks for installing MOKO SE.\nEnjoyable using!',
                         '@hello',
                         '3')

MOKO.StageSeparator()
MOKO.StageSeparator('NEXT SCRIPT')
MOKO.StageSeparator()

MOKO.ScriptEnd()