import time
import os
import sys
import RPi.GPIO as GPIO

global temp_sensor 
try: 
    import Adafruit_DHT
    sensor = Adafruit_DHT.DHT22
    pino_sensor = 21
    temp_sensor = True
except ImportError:
    temp_sensor = False
    print("Sem sensor de temperatura")
# I DONT HAVE RASPBERRY. DEBUG MODE

def init_board():
    GPIO.setmode(GPIO.BOARD)     
    GPIO.setwarnings(True)     

init_board()

def set_pin_as_output (pin_number):
    GPIO.setup (pin_number, GPIO.OUT)

def set_pin_as_input (pin_number):
    GPIO.setup (pin_number, GPIO.IN)

def write_to_port(pin_number, state):
    GPIO.output(pin_number, state)

def read_port(pin_number):
    return GPIO.input(pin_number)

def set_rele(pin_number, state):
    init_board()
    set_pin_as_output(pin_number)
    write_to_port(pin_number, state)

def get_umid_temp():
    if temp_sensor:
        umid, temp = None, None
        while umid == None and temp == None:
            umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor)
        temp_file = open("temp.txt", "w")
        temp_file.write(str(temp))
        temp_file.close()
    else:
        umid, temp = 73.5, 26.4 # For debug without rasp.
    return [temp, umid]

