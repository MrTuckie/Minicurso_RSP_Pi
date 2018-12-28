# Código feito por Arthur Lorencini Bergamaschi - UFES - Eng. Elétrica 2018

# Setup ---

# Importando as bibliotecas

import RPi.GPIO as GPIO # Lembrando que GPIO poderia ter qualquer outro nome.
                        # Utilizamos GPIO para facilitar.
import time
from time import sleep

# Definindo as opçoes da placa

GPIO.setwarnings(False) # Desabilita uma interrupcao por causa de um "Warning"
GPIO.setmode(GPIO.BOARD) # Definindo a orientaçao dos pinos

# Definindo o número dos pinos de saída

led_verde = 11
led_amarelo = 13
led_vermelho = 15
led_azul = 16

# Criando uma lista com esses valores

leds = [led_verde,led_amarelo,led_vermelho,led_azul]

# Definindo todos os pinos da lista como de saída e desligados

for x in leds:
    GPIO.setup(x, GPIO.OUT)
    GPIO.output(x,0)

# Loop ---

while(1):
    for x in leds:
        GPIO.output(x,1)
        sleep(1)
        GPIO.output(x,0)
        sleep(1)
