# Autor: Pedro Vinicius Custodio
## Código para usar o módulo A4988 e 2 chaves de fim de curso

import RPi.GPIO as GPIO
import time

# Usando a FakeRPiGPIO para testar o código. Remover próxima linha para usar na RaspberryPi | $ pip install fakeRPiGPIO
GPIO.VERBOSE = False

# Os pinos usados. Troque se quiser
direction = 11
step = 13
enable = 15

# Chaves de fim de curso
switchLeft = 23
switchRight = 24

# É exatamente isso. Sendo 0 a posição mais à esquerda.
currentPosition = 0

# A quantidade de passos dados para percorrer o eixo depende da configuração do módulo e da posição das chaves.
# O programa tem uma rotina que percorre o eixo para saber seu tamanho, em passos, steps do motor.
# É a posição mais à direita
axysSize = 0


# Valores positivos movem o eixo X passos para a direita e negativos X passos para a esquerda.
def moveAxys(steps):
    
    global currentPosition
    
    GPIO.output(enable, 0) # Habilita. A lógica é invertida
    GPIO.output(step, 0)
    
    if steps > 0:
        GPIO.output(direction, 1)
        inc = 1
    else:
        GPIO.output(direction, 0)
        inc = -1
        
    for i in range(0,abs(steps)):
        GPIO.output(step, 1)
        time.sleep(0.001) # Pode ser criada uma variável para alterar a velocidade do motor
        GPIO.output(step, 0)
        time.sleep(0.001)
        currentPosition = currentPosition + inc
    
    GPIO.output(enable, 1)

# Leva o eixo a qualquer posição entre 0 e axysSize.
def goto(position):
    
    global currentPosition
    global axysSize
    
    if position < 0:
        position = 0
    if position > axysSize:
        position = axysSize
        
    moveAxys(position - currentPosition)


# Início do programa

GPIO.setmode(GPIO.BOARD)

GPIO.setup(switchLeft, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switchRight, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(step, GPIO.OUT)
GPIO.setup(enable, GPIO.OUT)
GPIO.setup(direction, GPIO.OUT)

# LEIA-ME!
# Para testar, descomentar os fors e comentar os whiles.
# Faça o contrário para usar o código

while(GPIO.input(switchRight)):
#for i in range(0,5000): 
    moveAxys(1)

while(GPIO.input(switchLeft)):
#for i in range(0,5000):
    moveAxys(-1);
    axysSize = axysSize + 1

# Teste da função goto()
print ('goto(1500)')
goto(1500)
print ('goto(900)')
goto(900)

GPIO.cleanup()

def exit_handler():
    print ('Programa encerrado.\n Parando motor.')
    GPIO.cleanup()

atexit.register(exit_handler)
