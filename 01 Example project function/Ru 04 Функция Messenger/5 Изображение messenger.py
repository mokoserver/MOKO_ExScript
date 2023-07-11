import MOKO

#Region Status (статус)
#hesh Make screenshot
#hesh Save screenshot
#hesh Insert screenshot

MOKO.Messenger('set', 'Messenger - picture#@insert', 'В данном скрипте будет продемонстрирована вставка картинки в Messenger. '
                                                     'Для этого нужно сделать скриншот экрана командой '
                                                     'screenshot = MOKO.Program(\'control\', \'get\', \'screenshot\', \'string\'), '
                                                     'затем сохранить его '
                                                     'командой MOKO.Report(\'screenshot\', \'set\', \'picture\', screenshot).')

screenshot = MOKO.Program('control', 'get', 'screenshot', 'string')
MOKO.Program('tree', 'set', 'select = ' + 'Make screenshot')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Report('image_screenshot', 'set', 'picture', screenshot)
MOKO.Report("image_screenshot", 'save', 'picture', 'png')  
MOKO.Program('tree', 'set', 'select = ' + 'Save screenshot')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('tree', 'set', 'select = ' + 'Insert screenshot')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Messenger('set', 'image_screenshot.png', 'Скриншот программы MOKO SE вставлен выше.')

MOKO.EndScript()