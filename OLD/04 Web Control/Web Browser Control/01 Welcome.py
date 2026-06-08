
from datetime import datetime
import MOKO
import MOSC

# Fix script start time
StartTime = datetime.now()

# Initialize execution time report table
MOSC.InitScriptExecutionTime()

MOKO.Stage("Welcome to the Web Browser Control Project")

# Report execution time at the end
MOSC.ScriptExecutionTime(StartTime)

MOKO.EndScript()
