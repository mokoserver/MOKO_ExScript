import MOKO

#Region Status
#hesh Make screenshot
#hesh Save screenshot
#hesh Insert screenshot

MOKO.Messenger('set', 'Messenger - picture#@insert', 'This script will demonstrate how to insert a picture into Messenger. '
                                                     'To do this, take a screenshot of the screen with the command '
                                                     'screenshot = MOKO.Program(\'control\', \'get\', \'screenshot\', \'string\'), '
                                                     'then save it with the '
                                                     'command MOKO.Report(\'screenshot\', \'set\', \'picture\', screenshot).')

screenshot = MOKO.Program('control', 'get', 'screenshot', 'string')
MOKO.Program('tree', 'set', 'select = ' + 'Make screenshot')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Report('image_screenshot', 'set', 'picture', screenshot)
MOKO.Report("image_screenshot", 'save', 'picture', 'png')
MOKO.Program('tree', 'set', 'select = ' + 'Save screenshot')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('tree', 'set', 'select = ' + 'Insert screenshot')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Messenger('set', 'image_screenshot.png', 'Screenshot of MOKO SE program pasted above.')

MOKO.EndScript()