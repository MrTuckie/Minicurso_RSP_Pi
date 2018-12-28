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

led_vermelho = 15
led_azul = 16

# Criando uma lista com esses valores
leds = [led_vermelho,led_azul]

# Definindo todos os pinos da lista como de saída e desligados mais rápido
for x in leds:
    GPIO.setup(x, GPIO.OUT) # Define como pino de saída
    GPIO.output(x,0)        # Define que está em 0V - Nível lógico BAIXO

# Loop ---
while(1):
    for x in leds:
        GPIO.output(x,1)
        sleep(1)
        GPIO.output(x,0)
        sleep(1)
