import MOKO
import MTLG
import MOSC

MTLG.TelegramProgram('alpha', 'Проверка регистрации', 'set', 'Регистрация', 'string')
MOKO.Stage("*********************************************************")
MOKO.Stage("*************** Проверка регистрации ****************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

#region Регистрация оборудования$Reg
MOSC.HeshStatus("$Reg")
MOKO.Program('tree', 'set', 'select = Регистрация оборудования$Reg')

MOKO.Utility("IZRCSMinfo", "set", "Registration")

ProtocolNumber = MOKO.Utility("IZRCSMinfo", "get", "ProtocolNumber", "string")
CurrentDate = MOKO.Utility("IZRCSMinfo", "get", "CurrentDate", "string")
ModelDevice = MOKO.Utility("IZRCSMinfo", "get", "ModelDevice", "string")
SerialNumber = MOKO.Utility("IZRCSMinfo", "get", "SerialNumber", "string")
Owner = MOKO.Utility("IZRCSMinfo", "get", "owner", "string")
Request = MOKO.Utility("IZRCSMinfo", "get", "Request", "string")
Verifier = MOKO.Utility("IZRCSMinfo", "get", "Verifier", "string")
VerificationDate = MOKO.Utility("IZRCSMinfo", "get", "CurrentDate", "string")

MOKO.Report("REGISTRATION_ProtocolNumber", "info", "string", "Номер протокола измерения")
MOKO.Report("REGISTRATION_CurrentDate", "info", "string", "Текущая дата")
MOKO.Report("REGISTRATION_ModelDevice", "info", "string", "Модель тестируемого устройства")
MOKO.Report("REGISTRATION_SerialNumber", "info", "string", "Серийный номер устройства")
MOKO.Report("REGISTRATION_Owner", "info", "string", "Владелец")
MOKO.Report("REGISTRATION_Request", "info", "string", "Запрос")
MOKO.Report("REGISTRATION_Verifier", "info", "string", "Поверяющий")
MOKO.Report("REGISTRATION_VerificationDate", "info", "string", "Дата поверки")
MOKO.Report("REGISTRATION_FormNumber", "info", "string", "Номер формы")
MOKO.Report("REGISTRATION_GosNumber", "info", "string", "Номер измерения")

MOKO.Report("REGISTRATION_ProtocolNumber", "set", "string", ProtocolNumber)
MOKO.Report("REGISTRATION_CurrentDate", "set", "string", CurrentDate)
MOKO.Report("REGISTRATION_ModelDevice", "set", "string", ModelDevice)
MOKO.Report("REGISTRATION_SerialNumber", "set", "string", SerialNumber)
MOKO.Report("REGISTRATION_Owner", "set", "string", Owner)
MOKO.Report("REGISTRATION_Request", "set", "string", Request)
MOKO.Report("REGISTRATION_Verifier", "set", "string", Verifier)
MOKO.Report("REGISTRATION_VerificationDate", "set", "string", VerificationDate)
MOKO.Report("REGISTRATION_FormNumber", "set", "string", "432-164")
MOKO.Report("REGISTRATION_GosNumber", "set", "string", "52147-12")

MOKO.Utility("IZRCSMinfo", "set", "Conditions")

Temperature = MOKO.Utility("IZRCSMinfo", "get", "Temperature", "string")
Humidity = MOKO.Utility("IZRCSMinfo", "get", "Humidity", "string")
Pressure = MOKO.Utility("IZRCSMinfo", "get", "Pressure", "string")

MOKO.Report('VerificationConditions', 'info', 'table', "Controlled parameters#150;"
                                                       "ND requirements#100;"
                                                       "Measured values#100;")

MOKO.Report("VerificationConditions", "set", "table", f"Температура; 20°C; {Temperature}")
MOKO.Report("VerificationConditions", "set", "table", f"Влажность; 60%; {Humidity}")
MOKO.Report("VerificationConditions", "set", "table", f"Давление; 100kPa; {Pressure}")
MOKO.Stage(" ")

MOSC.hesh_passed()
#endregion Регистрация оборудования$Reg

MOKO.EndScript()
