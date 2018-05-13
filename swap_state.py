from devices import get_devices
import sys

print("Parametros: ", sys.argv)
device_name = sys.argv[1]
for device in get_devices():
    if device.name == device_name:
#         print(device)
#         pass
        device.swap_state()
    