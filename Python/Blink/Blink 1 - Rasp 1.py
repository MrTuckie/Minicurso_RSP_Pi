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


led_azul = 16
GPIO.setup(led_azul, GPIO.OUT) # Define como pino de saída
GPIO.output(led_azul,0)        # Define que está em 0V - Nível lógico BAIXO

# Loop ---

while(1):
    GPIO.output(led_azul,1)
    sleep(1)
    GPIO.output(led_azul,0)
    sleep(1)
