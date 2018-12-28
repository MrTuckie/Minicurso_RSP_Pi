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

# Definindo pino
botao_azul = 35


# Definindo quem é entrada e quem é saída

GPIO.setup(botao_azul, GPIO.IN) # Veremos coisas estranhas sem um resistor de pull up/down no circuito!

# Loop ---

while(1):
    i = GPIO.input(botao_azul) #  Armazena o valor do pino naquele instante
    if (i == 1): # Se a entrada estiver em nível lógico alto
        print("Nível lógico ALTO") # Teste do botão
    else:
        print("Nível lógico BAIXO")
    sleep(0.5) # Atualizando a leitura em pouco tempo
