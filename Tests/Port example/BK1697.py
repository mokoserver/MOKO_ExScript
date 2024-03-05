import MOKO

#Region Port
#hesh Port Testing

# timeout ???
device = 'BK'

result: str = MOKO.Port(device,'interface')
MOKO.Messenger('set', 'Answer from BK1697', f'result = {result}')

result: str = MOKO.Port(device,'init')
MOKO.Messenger('set', 'Answer from BK1697', f'result = {result}')

result: str = MOKO.Port(device,'write','GMAX00')
MOKO.Messenger('set', 'Answer from BK1697', f'result = {result}')

result: str = MOKO.Port(device,'read')
MOKO.Messenger('set', 'Answer from BK1697', f'result = {result}')

result: str = MOKO.Port(device,'read')
MOKO.Messenger('set', 'Answer from BK1697', f'result = {result}')

#EndRegion Region Status
MOKO.EndScript()
