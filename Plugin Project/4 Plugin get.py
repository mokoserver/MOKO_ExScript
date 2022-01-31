import MOKO
import MGPH

language = MOKO.Report("language", 'get', 'string', 'string', 'string')

#Region Status (статус)
#hesh Plugin get


if language == "English":
    MOKO.Messenger('set', 'Plugin - get.png', 'The current script will demonstrate the \'\'get\'\' command, '
                                                 'which receives data from the plugin. In the scripts will be made a screenshot.')

elif language == "Русский":
    MOKO.Messenger('set', 'Plugin - get.png', 'В текущем скрипте будет продемонстрирована команда \'\'get\'\', '
                                                 'которая передает данные в плагин. В данном скрипте будет сделан скриншот экрана')


screen = MGPH.GetScreenshotWindow()
MOKO.Report("Screenshot_1_All", 'set', 'picture', screen)

MOKO.Program('tree', 'set', 'select = ' + 'Plugin get')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.EndScript()