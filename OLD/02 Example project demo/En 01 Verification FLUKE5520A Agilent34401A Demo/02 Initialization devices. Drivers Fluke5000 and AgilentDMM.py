import MOKO
from SettingsAndMeasurement import Poverka

MOKO.Stage("*********************************************************")
MOKO.Stage("************ Initialization devices script **************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

MOKO.Stage("*********************************************************")
MOKO.Messenger("set", 'Connect device#@agilent34401a',
               'Сonnect the device under test via the interface\n'
               'Reference equipment: FLUKE5520.\n'
               'Verified equipment: AGILENT34401.\n'
               'Verification procedure: example.', delaytime='10')
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

#region Initialization AGILENT34401A$Init
MOKO.Program('tree', 'set', 'select = Initialization AGILENT34401A$Init')

Poverka.Agilent34401A.Initialization()

#endregion Initialization AGILENT34401A$Init

#region Initialization FLUKE5520A$Init
MOKO.Program('tree', 'set', 'select = Initialization FLUKE5520A$Init')

Poverka.Fluke5520A.Initialization()

#endregion Initialization FLUKE5520A$Init

MOKO.EndScript()
