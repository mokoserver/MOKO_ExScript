import MOKO

MOKO.Messenger('set', 'Greeting.jpg', 'Dear user! Right now, the work of the Graph plugin will be demonstrated to you. '
                                      'Happy viewing!')

#Region Status
#hesh Greeting
MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Region Status

MOKO.EndScript()