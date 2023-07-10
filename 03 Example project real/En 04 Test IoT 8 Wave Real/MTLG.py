import MOKO

scull_sml: str = '%E2%98%A0'
report_sml: str = '%F0%9F%93%A2'
driver_sml: str = '%F0%9F%96%A8'
prog_sml: str = '%F0%9F%85%BF'
message_sml: str = '%F0%9F%92%AC'
mode_sml: str = '%F0%9F%93%97'
name_sml: str = '%F0%9F%93%99'
head_sml: str = '%F0%9F%93%92'
command_sml: str = '%F0%9F%93%94'
type_sml: str = '%F0%9F%93%9A'
delay_sml: str = '%E2%8C%9B'
body_sml: str = '%F0%9F%93%B0'
data_sml: str = '%F0%9F%93%96'
information_source: str = '%E2%84%B9'


def TelegramReport(role: str, name: str, mode: str, kind: str, data: str, valuetype: str = 'void') -> None:

    MOKO.Telegram(role, 'set',
                  f'{report_sml} {report_sml} {report_sml} MOKO SE REPORT {report_sml} {report_sml} {report_sml}\n'
                  '\n'
                  f'{name_sml} NAME: {name}\n'
                  '\n'
                  f'{mode_sml} MODE: {mode}\n'
                  '\n'
                  f'{type_sml} KIND: {kind}\n'
                  '\n'
                  f'{data_sml} DATA: {data}\n'
                  '\n'
                  f'{type_sml} VALUETYPE: {valuetype}')


def TelegramMessenger(role: str, mode: str, head: str, body: str, valuetype: str = 'void', delaytime: str = 'void') -> None:
    MOKO.Telegram(role, 'set',
                  f'{message_sml} {message_sml} {message_sml} MOKO SE MESSENGER {message_sml} {message_sml} {message_sml}\n'
                  '\n'
                  f'{mode_sml} MODE: {mode}\n'
                  '\n'
                  f'{head_sml} HEAD: {head}\n'
                  '\n'
                  f'{body_sml} BODY: {body}\n'
                  '\n'
                  f'{type_sml} VALUETYPE: {valuetype}\n'
                  '\n'
                  f'{delay_sml} DELAYTIME: {delaytime}')


def TelegramPlugin(role: str, name: str, mode: str, command: str, valuetype: str = 'void') -> None:
    MOKO.Telegram(role, 'set',
                  f'{scull_sml} {scull_sml} {scull_sml} MOKO SE PLUGIN {scull_sml} {scull_sml} {scull_sml}\n'
                  '\n'
                  f'{name_sml} NAME: {name}\n'
                  '\n'
                  f'{mode_sml} MODE: {mode}\n'
                  '\n'
                  f'{command_sml} COMMAND: {command}\n'
                  '\n'
                  f'{type_sml} VALUETYPE: {valuetype}')


def TelegramUtility(role: str, name: str, mode: str, command: str, valuetype: str = 'void') -> None:
    MOKO.Telegram(role, 'set',
                  f'{scull_sml} {scull_sml} {scull_sml} MOKO SE UTILITY {scull_sml} {scull_sml} {scull_sml}\n'
                  '\n'
                  f'{name_sml} NAME: {name}\n'
                  '\n'
                  f'{mode_sml} MODE: {mode}\n'
                  '\n'
                  f'{command_sml} COMMAND: {command}\n'
                  '\n'
                  f'{type_sml} VALUETYPE: {valuetype}')


def TelegramProgram(role: str, name: str, mode: str, command: str, valuetype: str = 'void') -> None:
    MOKO.Telegram(role, 'set', f'{prog_sml} {prog_sml} {prog_sml} MOKO SE PROGRAM {prog_sml} {prog_sml} {prog_sml}\n'
                                  '\n'
                                  f'{name_sml} NAME: {name}\n'
                                  '\n'
                                  f'{mode_sml} MODE: {mode}\n'
                                  '\n'
                                  f'{command_sml} COMMAND: {command}\n'
                                  '\n'
                                  f'{type_sml} VALUETYPE: {valuetype}')


def TelegramClassic(role: str, mode: str, command: str, valuetype: str = 'void') -> None:
    MOKO.Telegram(role, 'set',
                  f'{scull_sml} {scull_sml} {scull_sml} MOKO SE TELEGRAM {scull_sml} {scull_sml} {scull_sml}\n'
                  '\n'
                  f'{name_sml} ROLE: {role}\n'
                  '\n'
                  f'{mode_sml} MODE: {mode}\n'
                  '\n'
                  f'{command_sml} COMMAND: {command}\n'
                  '\n'
                  f'{type_sml} VALUETYPE: {valuetype}')


def TelegramDriver(role: str, name: str, mode: str, command: str, valuetype: str = 'void') -> None:
    MOKO.Telegram(role, 'set',
                  f'{driver_sml} {driver_sml} {driver_sml} MOKO SE DRIVER {driver_sml} {driver_sml} {driver_sml}\n'
                  '\n'
                  f'{name_sml} NAME: {name}\n'
                  '\n'
                  f'{mode_sml} MODE: {mode}\n'
                  '\n'
                  f'{command_sml} COMMAND: {command}\n'
                  '\n'
                  f'{type_sml} VALUETYPE: {valuetype}')


def TelegramStage(role: str, stage_string: str, type: str) -> None:
    MOKO.Telegram(role, 'set',
                  f'{scull_sml} {scull_sml} {scull_sml} MOKO SE STAGE {scull_sml} {scull_sml} {scull_sml}\n'
                  '\n'
                  f'STAGE_STRING: {stage_string}\n'
                  '\n'
                  f'{type_sml} TYPE: {type}')


def TelegramEndScript(role: str, command: str = 'done') -> None:
    TelegramProgram(role, 'script', 'set', command)


