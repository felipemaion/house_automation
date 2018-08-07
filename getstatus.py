from devices import *
# ??? Eita... 
# devices = [abajur,ledpanel,computador,tv,ventilador,masturbador,microondas,radio]
devices = get_devices()
print("[", end="")
print(*devices, sep=",", end="]")