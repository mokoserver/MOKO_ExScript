import MOKO

MOKO.Stage("Начало скрипта")

#Region 4.1 Статус
#hesh Съем показаний

MOKO.Messenger('set', 'ELait03.jpg', 'В данном скрипте будет продемонстрирована работа с ELait3.', '', '5')
MOKO.Messenger('set', 'ELait03.jpg', 'Узнаем значение светового давления с помощью драйвера.' '', '5')
Lumen = MOKO.Driver('ELait03', 'get', 'Lumen', 'string')

MOKO.Messenger('set', 'ELait03.jpg', f'Текущее значение светового давления - {Lumen} кд/(м^2).', '', '3')

MOKO.Report('Lumen', 'set', 'string', f'{Lumen}')

MOKO.Program('tree', 'set', 'select = ' + 'Съем показаний')
MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion 4.1 Статус

MOKO.Stage("Конец скрипта")
MOKO.EndScript()

