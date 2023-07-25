import time

import MOKO

MOKO.Messenger('set', 'Info#@info', 'Open text document Autoit.txt located in '
                                    'C:\\MOKO SE\\Data and make any changes to it')

for _ in range(60):
    TextNotepad = MOKO.Autoit('*Autoit.txt', 'Edit1', 'ControlGetText', '')
    MOKO.Stage(f'Your text in Notepad: {TextNotepad}')
    MOKO.Report('TextNotepad','set','table',f'{TextNotepad}')
    time.sleep(1)

MOKO.EndScript()
