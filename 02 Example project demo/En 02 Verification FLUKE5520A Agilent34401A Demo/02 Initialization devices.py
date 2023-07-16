import MOKO
from ExFluke5000Agilent34401A_Demo import Poverka

MOKO.Stage("*********************************************************")
MOKO.Stage("************ Initialization devices script **************")
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

MOKO.Stage("*********************************************************")
MOKO.Messenger("set", 'Connect device#FLUKE5520A_AGILENT34401A.png',
               'Сonnect the device under test via the interface\n'
               'Reference equipment: FLUKE5520.\n'
               'Verified equipment: AGILENT34401.\n'
               'Verification procedure: example.', delaytime='10')
MOKO.Stage("*********************************************************")
MOKO.Stage(" ")

#region Initialization AGILENT34401$Init
MOKO.Program('tree', 'set', 'select = Initialization AGILENT34401$Init')

Poverka.InitializationAGILENT34401A()

#endregion Initialization AGILENT34401$Init

#region Initialization FLUKE5520A$Init
MOKO.Program('tree', 'set', 'select = Initialization FLUKE5520A$Init')

Poverka.InitializationFluke5520A()

#endregion Initialization FLUKE5520A$Init

MOKO.EndScript()
