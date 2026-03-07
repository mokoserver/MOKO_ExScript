import MOKO

#Region 1.1 Статус
#hash Приветствие

MOKO.Stage("Начало скрипта")
MOKO.Messenger('set', 'Greeting#@hello', 'В данном проекте будут показаны возможности чего-то там. Приятного просмотра!', '', '7')

MOKO.Program('tree', 'set', 'select = ' + 'Приветствие')
MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion 1.1 Статус

MOKO.Stage("Конец скрипта")

MOKO.EndScript()