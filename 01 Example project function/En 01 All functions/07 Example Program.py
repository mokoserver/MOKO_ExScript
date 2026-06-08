import MOKO
from MOSC import stars

MOKO.StageSeparator()
MOKO.StageSeparator('NEW SCRIPT')
MOKO.StageSeparator()


MOKO.StageInfo('*Program*')

MOKO.MessageSet( 'Program_info', 'This script implements one of the many functions of Program.')
MOKO.MessageSet( 'Program', 'The Program function is intended to control various elements from the script '
                                 'MOKO SE programs (scripts, project, control etc). '
                                 'Program has one mode of operation - \'\'set\'\', the function can only write '
                                 'certain commands.')
MOKO.ReportSave('Word')

MOKO.StageSeparator()
MOKO.StageSeparator('NEXT SCRIPT')
MOKO.StageSeparator()

MOKO.ScriptEnd()