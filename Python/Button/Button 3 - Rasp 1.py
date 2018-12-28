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


# Definindo pinos de saída e entrada

led_verde = 11
led_amarelo = 13
led_vermelho = 15
led_azul = 16
leds = [led_verde,led_amarelo,led_vermelho,led_azul]

botao_verde = 3
botao_amarelo = 5
botao_vermelho = 7
botao_azul = 8
botoes = [botao_verde,botao_amarelo,botao_vermelho,botao_azul]


for x in leds:
    GPIO.setup(x,GPIO.OUT)
    GPIO.output(x,0)


for x in botoes:
    GPIO.setup(x,GPIO.IN,GPIO.PUD_UP)


# Loop ---

while(1):
    for x in botoes:
        i = GPIO.input(x) #  Armazena o valor do pino naquele instante
        if (i == 1): # Se a entrada estiver em nível lógico alto
            print ("Pino %d - ON" % x)
        else:
            print ("Pino %d - OFF" % x)
    sleep(0.25) # Para fazer a leitura do pino
    #
