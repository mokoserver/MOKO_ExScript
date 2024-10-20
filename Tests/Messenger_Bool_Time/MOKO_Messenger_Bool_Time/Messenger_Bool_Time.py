import MOKO

#Region Тестирование

MOKO.Messenger('get', "Call #@callback.png", "Attention! No connection established. Do you want to look?! \nДолжен вернуться True (кнопка Yes)", 'bool=True time=6')
MOKO.Messenger('get', "Call #@callback.png", "Attention! No connection established. Do you want to look?! \nДолжен вернуться False (кнопка No)", 'bool=False time=6')

#EndRegion Тестирование

MOKO.EndScript('passed')