from datetime import datetime
import MOKO
import MOSC

StartTime = datetime.now()

MOKO.Program('tree', 'set', 'select = Шаг 4: Сохранить отчет$REPORT')
MOKO.Stage("--- Шаг 4: Сохранить отчет ---")
if MOSC.hashStatus('Шаг 4: Сохранить отчет$REPORT'):
    try:
        MOKO.Program('control', 'set', 'save word report')
        MOKO.Stage("Команда на генерацию Word-отчета отправлена.")
        MOSC.hash_passed()
    except Exception as e:
        MOKO.Stage(f"Ошибка во время генерации отчета: {e}", "error")
        MOSC.hash_failed()

MOSC.ScriptExecutionTime(StartTime)
MOKO.EndScript()
