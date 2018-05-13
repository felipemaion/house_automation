from corerasp import *
from device import Device

# abajur 1 pin7  (GPIO4)
# OFF 2 pin11 (GPIO17)
# OFF 3 pin12 (GPIO18)
# OFF 4 pin13 (GPIO27)
# OFF 5 pin15 (GPIO22)
# OFF 6 pin16 (GPIO23)
# OFF 7 pin18 (GPIO24)
# OFF 8 pin22 (GPIO25)

# IN THE FUTURE I MAY ADD THIS TO A CONFIG FILE, THAT CAN BE CFG BY WEB. TODO: 
abajur = Device(pin=7,io="OUT",description="ABAJUR",high=1)
ledpanel = Device(11,"OUT","LED PANEL",0)
computador = Device(12,"OUT","COMPUTADOR",0)
tv = Device(13,"OUT","TV",0)
ventilador = Device(15,"OUT","VENTILADOR",0)
masturbador = Device(16,"OUT","MASTURBADOR",0)
microondas = Device(18,"OUT","FORNO MICROONDAS",0)
radio = Device(22,"OUT","RADIO",0)
devices = [abajur,ledpanel,computador,tv,ventilador,masturbador,microondas,radio]

def get_devices():
    return devices