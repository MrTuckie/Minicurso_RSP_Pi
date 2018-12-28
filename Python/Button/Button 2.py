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

# Definindo quem é entrada e saída

botao_azul = 35
led_azul = 40
GPIO.setup(botao_azul, GPIO.IN, GPIO.PUD_UP) # Ativa um resistor de pull up
GPIO.setup(led_azul, GPIO.OUT)


# Loop ---

while(1):
    i = GPIO.input(botao_azul) #  Armazena o valor do pino naquele instante
    if (i == 1): # Se a entrada estiver em nível lógico alto
        print("Nível lógico ALTO") # Teste do botão
        GPIO.output(led_azul,1)
    else:
        print("Nível lógico BAIXO")
        GPIO.output(led_azul,0)

#
