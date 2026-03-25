from datetime import datetime
import MOKO
import MOSC

StartTime = datetime.now()

MOSC.InitScriptExecutionTime()

MOKO.Stage("Добро пожаловать в проект управления веб‑браузером")

MOSC.ScriptExecutionTime(StartTime)

MOKO.EndScript()
