# -*- coding: utf-8 -*-
# Atuador conforme temperatura pre-definida
# Autor : FELIPE MAION
import RPi.GPIO as GPIO  #biblioteca GPIO

import Adafruit_DHT

import time
import os


# Define o tipo de sensor
#sensor = Adafruit_DHT.DHT11
sensor = Adafruit_DHT.DHT22

GPIO.setmode(GPIO.BOARD)

# Define a GPIO conectada ao pino de dados do sensor
pino_sensor = 21


# Código extraido do automate.py para inicializar o relé.
def inicializaBoard():
    GPIO.setmode(GPIO.BOARD)     #Utilizando a referencias do pinos
    GPIO.setwarnings(False)     #desabilita as mensagens

def definePinoComoSaida (numeroPino):
    GPIO.setup (numeroPino, GPIO.OUT)

def escreveParaPorta(numeroPino, estadoPorta):
    GPIO.output(numeroPino, estadoPorta)

def liga_rele(numeroPino, estadoPorta):
    inicializaBoard()
    definePinoComoSaida(numeroPino)
    escreveParaPorta(numeroPino, estadoPorta)
flag = None
# Informacoes iniciais
print ("*** Lendo os valores de temperatura e umidade")
while(1):
    print (time.asctime())
    # Efetua a leitura do sensor
    umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor)
    # Caso leitura esteja ok, mostra os valores na tela
    if umid is not None and temp is not None:
        print ("\033[4;30;43mTemperatura = {0:0.1f} Umidade = {1:0.1f}\33[m").format(temp, umid);
        if float("{0:0.1f}".format(temp)) >= float("{0:0.1f}".format(30.0)):
            liga_rele(7,0)
            if not flag or flag == "down":
                os.system('omxplayer /home/pi/Downloads/1815.mp3')
                flag = "up"
        if float("{0:0.1f}".format(temp)) <= float("{0:0.1f}".format(26.0)):
            liga_rele(7,1)
            if not flag or flag == "up":
                os.system('omxplayer /home/pi/Downloads/1815_2.mp3')
                flag = "down"
        time.sleep (10) # 10 s para depurar...
        print ("Aguarda 2 minutos (10 seg debug) para efetuar nova leitura...");
    else:
        # Mensagem de erro de comunicacao com o sensor
        print("Falha ao ler dados do DHT22 !!!")

# OBS: este script eu salvo como temperatura.sh e executo via terminal para ler a temperatura.

# #Código que aciona relê
# # Script que desliga Relê
# #!/bin/bash
# cd /home/pi/GPIO
# python automate.py 7 1
# #git pull
# bash
# exit




