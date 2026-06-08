import MOKO as Moko
from MOSC import stars
import time

Moko.Stage(stars('*'))
Moko.Stage(stars('NEW SCRIPT'))
Moko.Stage(stars('*'))

Moko.Stage('Welcome to MOKO SE.')
Moko.Stage('MOKO SE manages MOKO NMEA program and driver software.')
Moko.Stage('Program control is implemented through the execution of scripts written in Python.')
Moko.Stage('This script shows how the Stage function works.')
Moko.Stage('Stage messages can be of a specific type. Each of the types is presented below.')
Moko.Stage('*Info*. Outputs any information to Stage. Designated as default type', 'Info')
Moko.Stage('*Success*. Outputs any information to Stage. Designated as default type', 'Success')
Moko.Stage('*Fail*. Outputs any information to Stage. Designated as default type', 'Fail')
Moko.Stage('*Error*. Informs about an error that occurred during script execution.', 'Error')
Moko.Stage('*Plugin*. Displays information related to a plugin.', 'Plugin')
Moko.Stage('*Driver*. Displays information related to the driver.', 'Driver')
Moko.Stage('*Report*. Informs about data recording in the report.', 'Report')
Moko.Stage('*Utility*. Reports the use of the utility.', 'Utility')
Moko.Stage('*Message*. Informs about the Messenger window display.', 'Message')
Moko.Stage('*Telegram*. afafafaf', 'Telegram')
Moko.Stage('*Warning*. Informs about an warning that occurred during script execution.', 'Warning')
time.sleep(6)
Moko.Report("exstage", 'set', 'string', 'Absent')
Moko.Report("exstage_1", 'set', 'string', 'The script completed successfully.')

Moko.Stage(stars('*'))
Moko.Stage(stars('NEXT SCRIPT'))
Moko.Stage(stars('*'))

Moko.EndScript()