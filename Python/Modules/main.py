import RPi.GPIO as GPIO
import time
from time import sleep

# importando o módulo criado

import led

# Definindo as opçoes da placa

GPIO.setwarnings(False) # Desabilita uma interrupcao por causa de um "Warning"
GPIO.setmode(GPIO.BOARD) # Definindo a orientaçao dos pinos

# Definindo o número dos pinos de saída

led_verde = 36
led_amarelo = 38
led_vermelho = 37
led_azul = 40

# Criando uma lista com esses valores

leds = [led_verde,led_amarelo,led_vermelho,led_azul]

# Definindo todos os pinos da lista como de saída e desligados

for x in leds:
    GPIO.setup(x, GPIO.OUT)
    GPIO.output(x,0)

led.pisca(5,led_azul)
