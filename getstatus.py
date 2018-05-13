from devices import *

devices = [abajur,ledpanel,computador,tv,ventilador,masturbador,microondas,radio]
print("[", end="")
print(*devices, sep=",", end="]")