import MOKO
from MOSC import stars
import time


MOKO.StageSeparator()
MOKO.StageSeparator('NEW SCRIPT')
MOKO.StageSeparator()

MOKO.Stage('Welcome to MOKO SE.')

MOKO.StageSeparator()

MOKO.Stage('MOKO SE manages MOKO NMEA program and driver software.')
MOKO.Stage('Program control is implemented through the execution of scripts written in Python.')
MOKO.Stage('This script shows how the Stage function works.')
MOKO.Stage('Stage messages can be of a specific type. Each of the types is presented below.')

MOKO.StageSeparator()

MOKO.StageInfo('*Info*. Outputs any information to Stage. Designated as default type')
MOKO.StageSuccess('*Success*. Outputs any information to Stage. Designated as default type')
MOKO.StageFail('*Fail*. Outputs any information to Stage. Designated as default type')
MOKO.StageError('*Error*. Informs about an error that occurred during script execution.')
MOKO.StagePlugin('*Plugin*. Displays information related to a plugin.')
MOKO.StageDriver('*Driver*. Displays information related to the driver.')
MOKO.StageReport('*Report*. Informs about data recording in the report.')
MOKO.StageUtility('*Utility*. Reports the use of the utility.')
MOKO.StageMessage('*Message*. Informs about the Messenger window display.')
MOKO.StageTelegram('*Telegram*. afafafaf')
MOKO.StageMax('*Telegram*. afafafaf')
MOKO.StageWarning('*Warning*. Informs about an warning that occurred during script execution.')

MOKO.StageSeparator('Wait 3 secconds')
time.sleep(3)

MOKO.StageSeparator()
MOKO.ReportSetString("exstage", 'Absent')
MOKO.ReportSetString("exstage_1", 'The script completed successfully.')

MOKO.StageSeparator()
MOKO.StageSeparator('NEXT SCRIPT')
MOKO.StageSeparator()

MOKO.ScriptEnd()