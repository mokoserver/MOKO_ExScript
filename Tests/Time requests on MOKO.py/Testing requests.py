import time

import MOKO

x = 0

start_time = time.time()

for x in range(100):
    MOKO.Stage(f'Test requests number {x + 1}')
    MOKO.Report(f'test {x + 1}', 'set', 'string', 'OK')
    MOKO.Messenger('set', f'Test number {x + 1}#@repeat', f'Test number {x + 1}: status OK', delaytime='2')

end_time = time.time()
execution_time = end_time - start_time

MOKO.Messenger('set', 'Script executed#@punk', f'Script execution time: '
                                               f'{round(execution_time, 5)} on {x + 1} tests')
MOKO.EndScript()
