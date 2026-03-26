import MOKO
import MTLG
import MOSC

MTLG.TelegramProgram('alpha', 'Registration unit', 'set', 'registration')
MOKO.Stage("*********************************************************")
MOKO.Stage("*************** Registration unit script ****************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

info = "TestInfo"
#region Equipment registration$Reg
MOSC.hashStatus("$Reg")
MOKO.Program('tree', 'set', 'select = Equipment registration$Reg')

MOKO.Utility(info, "set", "Registration")

ProtocolNumber = MOKO.Utility(info, "get", "ProtocolNumber", "string")
CurrentDate = MOKO.Utility(info, "get", "CurrentDate", "string")
ModelDevice = MOKO.Utility(info, "get", "ModelDevice", "string")
SerialNumber = MOKO.Utility(info, "get", "SerialNumber", "string")
Owner = MOKO.Utility(info, "get", "owner", "string")
Request = MOKO.Utility(info, "get", "Request", "string")
Verifier = MOKO.Utility(info, "get", "Verifier", "string")
VerificationDate = MOKO.Utility(info, "get", "CurrentDate", "string")

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

MOKO.Utility(info, "set", "Conditions")

Temperature = MOKO.Utility(info, "get", "Temperature", "string")
Humidity = MOKO.Utility(info, "get", "Humidity", "string")
Pressure = MOKO.Utility(info, "get", "Pressure", "string")

MOKO.Report('VerificationConditions', 'info', 'table', "Controlled parameters#150;"
                                                       "ND requirements#100;"
                                                       "Measured values#100;")

MOKO.Report("VerificationConditions", "set", "table", f"Temperature; 20°C; {Temperature}")
MOKO.Report("VerificationConditions", "set", "table", f"Humidity; 60%; {Humidity}")
MOKO.Report("VerificationConditions", "set", "table", f"Pressure; 100kPa; {Pressure}")
MOKO.Stage(" ")

MOSC.hash_passed()
#endregion Equipment registration$Reg

MOKO.EndScript()
