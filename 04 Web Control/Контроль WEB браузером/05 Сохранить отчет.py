import MOKO
from MOKO import Stage, StageError, StageInfo,StageSuccess

#region Создание протокола$REPORT
#description: MS Word;
MOKO.ExecuteStep("Создание протокола$REPORT")

if MOKO.SelectCheckHash('Создание протокола$REPORT'):
    try:
        MOKO.SaveReport("Word")
        MOKO.StageSuccess("Word-отчет сгенерирован")
        MOKO.SetHash('passed')
    except Exception as e:
        MOKO.StageError(f"Ошибка во время генерации отчета: {e}")
        MOKO.SetHash('failed')

MOKO.TimeReport('add',"RU")
MOKO.EndScript()
