# import RPi.GPIO as GPIO
import sys

# # Define o tipo de sensor
# # DEBUG:
# sensor = Adafruit_DHT.DHT22
# GPIO.setmode(GPIO.BOARD)

# Define a GPIO conectada ao pino de dados do sensor
pino_sensor = 21

def get_umid_temp():
    # umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor)
    umid, temp = 73.5, 26.4 # For debug without rasp.
    return [str(temp), str(umid)]


# sys.stdout.write(','.join(get_umid_temp()))
print(",".join(get_umid_temp()))