from datetime import datetime
import MOKO
import MOSC

StartTime = datetime.now()

MOKO.Program('tree', 'set', 'select = Step 4: Save Report$REPORT')
MOKO.Stage("--- Step 4: Save Report ---")
if MOSC.hashStatus('Step 4: Save Report$REPORT'):
    try:
        MOKO.Program('control', 'set', 'save word report')
        MOKO.Stage("Word report generation command sent.")
        MOSC.hash_passed()
    except Exception as e:
        MOKO.Stage(f"Error during report generation: {e}", "error")
        MOSC.hash_failed()

MOSC.ScriptExecutionTime(StartTime)
MOKO.EndScript()
