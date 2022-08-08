import MOKO
import random

scull_sml = '%E2%98%A0'
report_sml = '%F0%9F%93%A2'#'%F0%9F%97%9E'#'%F0%9F%93%87'#'%F0%9F%93%9C'
driver_sml = '%F0%9F%96%A8'
prog_sml = '%F0%9F%85%BF'
message_sml = '%F0%9F%92%AC'

mode_sml = '%F0%9F%93%97'
name_sml = '%F0%9F%93%99'
head_sml = '%F0%9F%93%92'
command_sml = '%F0%9F%93%94'
type_sml = '%F0%9F%93%9A'
delay_sml = '%E2%8C%9B'
body_sml = '%F0%9F%93%B0'
data_sml = '%F0%9F%93%96'

def TelegramReport(name, mode, kind, data, valuetype='void'):
    MOKO.Telegram('alpha', 'set', f'{report_sml} {report_sml} {report_sml} MOKO SE REPORT {report_sml} {report_sml} {report_sml}\n'
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

def TelegramMessenger(mode, head, body, valuetype='void', delaytime='void'):
    MOKO.Telegram('alpha', 'set', f'{message_sml} {message_sml} {message_sml} MOKO SE MESSENGER {message_sml} {message_sml} {message_sml}\n'
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

def TelegramPlugin(name, mode, command, valuetype='void'):
    MOKO.Telegram('alpha', 'set', f'{scull_sml} {scull_sml} {scull_sml} MOKO SE PLUGIN {scull_sml} {scull_sml} {scull_sml}\n'
                                  '\n'
                                  f'{name_sml} NAME: {name}\n'
                                  '\n'
                                  f'{mode_sml} MODE: {mode}\n'
                                  '\n'
                                  f'{command_sml} COMMAND: {command}\n'
                                  '\n'
                                  f'{type_sml} VALUETYPE: {valuetype}')

def TelegramUtility(name, mode, command, valuetype='void'):
    MOKO.Telegram('alpha', 'set', f'{scull_sml} {scull_sml} {scull_sml} MOKO SE UTILITY {scull_sml} {scull_sml} {scull_sml}\n'
                                  '\n'
                                  f'{name_sml} NAME: {name}\n'
                                  '\n'
                                  f'{mode_sml} MODE: {mode}\n'
                                  '\n'
                                  f'{command_sml} COMMAND: {command}\n'
                                  '\n'
                                  f'{type_sml} VALUETYPE: {valuetype}')

def TelegramProgram(name, mode, command, valuetype='void'):
    MOKO.Telegram('alpha', 'set', f'{prog_sml} {prog_sml} {prog_sml} MOKO SE PROGRAM {prog_sml} {prog_sml} {prog_sml}\n'
                                  '\n'
                                  f'{name_sml} NAME: {name}\n'
                                  '\n'
                                  f'{mode_sml} MODE: {mode}\n'
                                  '\n'
                                  f'{command_sml} COMMAND: {command}\n'
                                  '\n'
                                  f'{type_sml} VALUETYPE: {valuetype}')

def TelegramClassic(role, mode, command, valuetype='void'):
    MOKO.Telegram('alpha', 'set', f'{scull_sml} {scull_sml} {scull_sml} MOKO SE TELEGRAM {scull_sml} {scull_sml} {scull_sml}\n'
                                  '\n'
                                  f'{name_sml} ROLE: {role}\n'
                                  '\n'
                                  f'{mode_sml} MODE: {mode}\n'
                                  '\n'
                                  f'{command_sml} COMMAND: {command}\n'
                                  '\n'
                                  f'{type_sml} VALUETYPE: {valuetype}')

def TelegramDriver(name, mode, command, valuetype='void'):
    MOKO.Telegram('alpha', 'set', f'{driver_sml} {driver_sml} {driver_sml} MOKO SE DRIVER {driver_sml} {driver_sml} {driver_sml}\n'
                                  '\n'
                                  f'{name_sml} NAME: {name}\n'
                                  '\n'
                                  f'{mode_sml} MODE: {mode}\n'
                                  '\n'
                                  f'{command_sml} COMMAND: {command}\n'
                                  '\n'
                                  f'{type_sml} VALUETYPE: {valuetype}')

def TelegramStage(stage_string, type):
    MOKO.Telegram('alpha', 'set', f'{scull_sml} {scull_sml} {scull_sml} MOKO SE STAGE {scull_sml} {scull_sml} {scull_sml}\n'
                                  '\n'
                                  f'STAGE_STRING: {stage_string}\n'
                                  '\n'
                                  f'{type_sml} TYPE: {type}')

def TelegramEndScript(command='done'):
    TelegramProgram('script', 'set', command)