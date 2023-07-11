import MOKO
import MOSC

MOKO.Stage("*********************************************************")
MOKO.Stage("*************** Registration unit script ****************")
MOKO.Stage("*********************************************************")

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

MOKO.Report("ProtocolNumber", "info", "string", "Measurement protocol number")
MOKO.Report("CurrentDate", "info", "string", "The current date")
MOKO.Report("ModelDevice", "info", "string", "Model of device under test")
MOKO.Report("SerialNumber", "info", "string", "Device serial number")
MOKO.Report("Owner", "info", "string", "Customer")
MOKO.Report("Request", "info", "string", "Request")
MOKO.Report("Verifier", "info", "string", "Verifier")
MOKO.Report("VerificationDate", "info", "string", "The verification date")
MOKO.Report("FormNumber", "info", "string", "Form number")
MOKO.Report("GosNumber", "info", "string", "Measurement number")

MOKO.Report("ProtocolNumber", "set", "string", ProtocolNumber)
MOKO.Report("CurrentDate", "set", "string", CurrentDate)
MOKO.Report("ModelDevice", "set", "string", ModelDevice)
MOKO.Report("SerialNumber", "set", "string", SerialNumber)
MOKO.Report("Owner", "set", "string", Owner)
MOKO.Report("Request", "set", "string", Request)
MOKO.Report("Verifier", "set", "string", Verifier)
MOKO.Report("VerificationDate", "set", "string", VerificationDate)
MOKO.Report("FormNumber", "set", "string", "432-164")
MOKO.Report("GosNumber", "set", "string", "52147-12")

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

text_report_fluke = "U=(34mV-1000V), Error±(0,0012-0,005)%, 2nd category\\nI=(24mkA-10A), Error±(0,011-0,1)%, " \
    "1 category\\nU~(25mV-1000V), 10Hz-500kHz, Error±(0,017-1)% 2nd category\\nI~=(2mkA-10A), 20Hz-20kHz, " \
    "Error±(0,046-3,02)%, 2nd category\\nR=(0,5О[[Ohm]]-5О[Ohm]), (110M[Ohm]-1100M[Ohm]), Error ±(0,33-2)%, 3nd category"
text_report_voltmeter = "U=(0,001V-1000V), Error±(0,000315 – 0,0011)%  2-nd category\\nU~=(0.75mV-1000V), " \
                        "10Hz-50kHz, Error±(0,003 – 0,23)%, 2-nd category\\nI=(70nA-30A), Error±(0,00275 – 0,05)%, " \
                        "1 category\\nI~=(70nA-20A), 0,1Hz-10kHz, Error±(0,0165 – 0,55)%, 2-nd category"

MOKO.Report('VerificationTools', 'info', 'table', "Name, type, serial number#350;"
                                                  "Metrological characteristics#400;")

MOKO.Report("VerificationTools", "set", "table", f"Fluke 5522A Multifunctional Calibrator Serial №2182904; "
            f"{text_report_fluke}")
MOKO.Report("VerificationTools", "set", "table", f"Universal voltmeter calibrator H4-12 Serial №005211; "
            f"{text_report_voltmeter}")

MOSC.hesh_passed()
#endregion Equipment registration$Reg

MOKO.EndScript()
