import MOKO

MOKO.Report('Messenger', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')
MOKO.Report('Messenger_clear', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')
MOKO.Report('Messenger_delete', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')

MOKO.Report(f'Messenger', 'set', 'table', '1;2;3;4;5;6;7;8;9')
MOKO.Report(f'Messenger_clear', 'set', 'table', '1;2;3;4;5;6;7;8;9')
MOKO.Report(f'Messenger_delete', 'set', 'table', '1;2;3;4;5;6;7;8;9')
#Region Status (статус)
#hash Greeting

MOKO.Messenger('set', 'Приветствие#@hello', 'В текущем проекте будут показаны дополнительные возможности Messenger.')

MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

MOKO.EndScript()