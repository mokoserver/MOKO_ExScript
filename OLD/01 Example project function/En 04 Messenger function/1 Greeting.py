import MOKO

MOKO.Report('Messenger', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')
MOKO.Report('Messenger_clear', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')
MOKO.Report('Messenger_delete', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')

MOKO.Report(f'Messenger', 'set', 'table', '1;2;3;4;5;6;7;8;9')
MOKO.Report(f'Messenger_clear', 'set', 'table', '1;2;3;4;5;6;7;8;9')
MOKO.Report(f'Messenger_delete', 'set', 'table', '1;2;3;4;5;6;7;8;9')
#Region Status
#hash Greeting

MOKO.Messenger('set', 'Greeting#@hello', 'Additional features of Messenger will be shown in the current project.')

MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

MOKO.EndScript()