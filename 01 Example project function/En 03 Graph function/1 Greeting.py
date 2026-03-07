import MOKO

MOKO.Messenger('set', 'Greeting#@hello', 'Dear user! Right now, the work of the Graph plugin will be demonstrated to you. '
                                      'Happy viewing!')

#Region Status
#hash Greeting
MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status

MOKO.EndScript()