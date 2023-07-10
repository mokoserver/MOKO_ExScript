import MOKO
import MTLG
import MOSC

MTLG.TelegramProgram('alpha', 'Registration unit', 'set', 'registration', 'string')
MOKO.Stage("*********************************************************")
MOKO.Stage("*************** Registration unit script ****************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

#region Equipment registration$Reg
MOSC.HeshStatus("$Reg")
MOKO.Program('tree', 'set', 'select = Equipment registration$Reg')

MOKO.Utility("IZRCSM", "set", "Registration")

ProtocolNumber = MOKO.Utility("IZRCSM", "get", "ProtocolNumber", "string")
CurrentDate = MOKO.Utility("IZRCSM", "get", "CurrentDate", "string")
ModelDevice = MOKO.Utility("IZRCSM", "get", "ModelDevice", "string")
SerialNumber = MOKO.Utility("IZRCSM", "get", "SerialNumber", "string")
Owner = MOKO.Utility("IZRCSM", "get", "owner", "string")
Request = MOKO.Utility("IZRCSM", "get", "Request", "string")
Verifier = MOKO.Utility("IZRCSM", "get", "Verifier", "string")
VerificationDate = MOKO.Utility("IZRCSM", "get", "CurrentDate", "string")

MOKO.Report("REGISTRATION_ProtocolNumber", "info", "string", "Measurement protocol number")
MOKO.Report("REGISTRATION_CurrentDate", "info", "string", "The current date")
MOKO.Report("REGISTRATION_ModelDevice", "info", "string", "Model of device under test")
MOKO.Report("REGISTRATION_SerialNumber", "info", "string", "Device serial number")
MOKO.Report("REGISTRATION_Owner", "info", "string", "Customer")
MOKO.Report("REGISTRATION_Request", "info", "string", "Request")
MOKO.Report("REGISTRATION_Verifier", "info", "string", "Verifier")
MOKO.Report("REGISTRATION_VerificationDate", "info", "string", "The verification date")
MOKO.Report("REGISTRATION_FormNumber", "info", "string", "Form number")
MOKO.Report("REGISTRATION_GosNumber", "info", "string", "Measurement number")

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

MOKO.Utility("IZRCSM", "set", "Conditions")

Temperature = MOKO.Utility("IZRCSM", "get", "Temperature", "string")
Humidity = MOKO.Utility("IZRCSM", "get", "Humidity", "string")
Pressure = MOKO.Utility("IZRCSM", "get", "Pressure", "string")

MOKO.Report('VerificationConditions', 'info', 'table', "Controlled parameters#150;"
                                                       "ND requirements#100;"
                                                       "Measured values#100;")

MOKO.Report("VerificationConditions", "set", "table", f"Temperature; 20°C; {Temperature}")
MOKO.Report("VerificationConditions", "set", "table", f"Humidity; 60%; {Humidity}")
MOKO.Report("VerificationConditions", "set", "table", f"Pressure; 100kPa; {Pressure}")
MOKO.Stage(" ")

MOSC.hesh_passed()
#endregion Equipment registration$Reg

MOKO.EndScript()
