import MOKO
import MGPH

#Region Status (статус)
#hesh Plugin get

MOKO.Messenger('set', 'Plugin - get.png', 'В текущем скрипте будет продемонстрирована команда \'\'get\'\', '
                                          'которая передает данные в плагин. '
                                          'В данном скрипте будет сделан скриншот экрана')


screen = MGPH.GetScreenshotWindow()
MOKO.Report("Screenshot_1_All", 'set', 'picture', screen)

MOKO.Program('tree', 'set', 'select = ' + 'Plugin get')
MOKO.Program('tree', 'set', 'chosen = passed')

MOKO.EndScript()
