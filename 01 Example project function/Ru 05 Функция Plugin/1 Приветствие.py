import MOKO

#Region Status (статус)
#hesh Greeting

MOKO.Messenger('set', 'Приветствие#@hello', 'В текущем проекте будут показаны возможности управления плагином. '
                                         'В данном примере всё будет показываться на основе плагина Graph.')

MOKO.Program('tree', 'set', 'select = ' + 'Greeting')
MOKO.Program('tree', 'set', 'chosen = passed')
# EndRegion Status

MOKO.EndScript()
