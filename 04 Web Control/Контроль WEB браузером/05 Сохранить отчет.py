import MOKO
from MOKO import Stage, StageError, StageInfo,StageSuccess

#region Создание протокола$REPORT
#description: MS Word;
MOKO.HashExecuteStep("Создание протокола$REPORT")

if MOKO.HashSelectCheck('Создание протокола$REPORT'):
    try:
        MOKO.ReportSave("Word")
        MOKO.StageSuccess("Word-отчет сгенерирован")
        MOKO.HashSet('passed')
    except Exception as e:
        MOKO.StageError(f"Ошибка во время генерации отчета: {e}")
        MOKO.HashSet('failed')

MOKO.ReportTimeAdd('add',"RU")
MOKO.EndScript()
