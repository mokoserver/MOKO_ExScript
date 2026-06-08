import MOKO

#Region Status
#hash Greeting

MOKO.Messenger('set', 'Greeting#@hello', 'The current project will show the plugin\'s control options. '
                                      'In this example, everything will be shown based on the Graph plugin.')

MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

MOKO.EndScript()
