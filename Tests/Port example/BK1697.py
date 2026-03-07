import MOKO


def work_bk1697(device: str):
    ok_result: str = '402502'
    is_init = init_device(device=device)
    while True:
        if not is_init:
            result_interface = call_interface(device=device)
            if result_interface:
                is_init = init_device(device=device)
        if is_init:
            result_write_command = write_command(device=device)
            if result_write_command:
                result_command = read_command(device=device)
                result_status = read_command(device=device)
                if result_status == 'OK' and result_command == ok_result:
                    MOKO.Stage(stage_string='Status: successful')
                    break
                else:
                    is_init = False
                    MOKO.Stage(type='warning', stage_string=f'Status: failed; {(
                        'Result stasus = failed' if not result_status else 'Result command != required result')}')


def init_device(device: str) -> bool:
    MOKO.Stage('')
    MOKO.Stage('******************************************************************************************************')
    result: str = MOKO.Port(name=device, mode='init')
    MOKO.Stage(stage_string=f"Block init device. Result = {result}", type='info' if result == 'ok' else 'warning')
    return result == 'ok'


def call_interface(device: str) -> bool:
    MOKO.Stage('')
    MOKO.Stage('******************************************************************************************************')
    result: str = MOKO.Port(name=device, mode='interface')
    MOKO.Stage(stage_string=f"Block call interface. Result = {result}", type='info' if result == 'ok' else 'warning')
    MOKO.Stage('******************************************************************************************************')
    return result == 'ok'


def write_command(device: str) -> bool:
    MOKO.Stage('')
    MOKO.Stage('******************************************************************************************************')
    result: str = MOKO.Port(name=device, mode='write', command='GMAX00')
    MOKO.Stage(stage_string=f"Block write command. Result = {result}", type='info' if result != 'error' else 'warning')
    MOKO.Stage('******************************************************************************************************')
    return result != 'error'


def read_command(device: str) -> str:
    MOKO.Stage('')
    MOKO.Stage('******************************************************************************************************')
    result: str = MOKO.Port(name=device, mode='read')
    MOKO.Stage(stage_string=f"Block read result command. Result = {result}")
    MOKO.Stage('******************************************************************************************************')
    return result


#Region Port
#hash Port Testing

work_bk1697(device="BK")

#EndRegion Region Status
MOKO.EndScript()
