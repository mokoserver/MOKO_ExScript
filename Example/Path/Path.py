import MOKO

language = MOKO.Report("language", 'get', 'string', 'string', 'string')

#Region Status (статус)
#hesh Make screenshot
#hesh Save screenshot
#hesh Insert screenshot

if language == "English":
    MOKO.Messenger('set', 'Messenger - picture.jpg', 'This script will demonstrate how to insert a picture into Messenger. '
                                                     'To do this, take a screenshot of the screen with the command '
                                                     'screenshot = MOKO.Program(\'control\', \'get\', \'screenshot\', \'string\'), '
                                                     'then save it with the '
                                                     'command MOKO.Report(\'screenshot\', \'set\', \'picture\', screenshot).')

elif language == "Русский":
    MOKO.Messenger('set', 'Messenger - picture.jpg', 'В данном скрипте будет продемонстрирована вставка картинки в Messenger. '
                                                     'Для этого нужно сделать скриншот экрана командой '
                                                     'screenshot = MOKO.Program(\'control\', \'get\', \'screenshot\', \'string\'), '
                                                     'затем сохранить его '
                                                     'командой MOKO.Report(\'screenshot\', \'set\', \'picture\', screenshot).')

screenshot = MOKO.Program('control', 'get', 'screenshot', 'string')
MOKO.Program('tree', 'set', 'select = ' + 'Make screenshot')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Report('image_screenshot', 'set', 'picture', screenshot)
MOKO.Report("image_screenshot", 'save', 'picture', 'png')  # В отдельный скрипт
MOKO.Program('tree', 'set', 'select = ' + 'Save screenshot')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.Program('tree', 'set', 'select = ' + 'Insert screenshot')
MOKO.Program('tree', 'set', 'chosen = passed')

if language == "English":
    MOKO.Messenger('set', 'image_screenshot.png', 'Screenshot of MOKO SE program pasted above.')
elif language == "Русский":
    MOKO.Messenger('set', 'image_screenshot.png', 'Скриншот программы MOKO SE вставлен выше.')


MOKO.EndScript()