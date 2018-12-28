# Autor: Pedro Vinicius Custodio
## Código para usar o módulo A4988 e 2 chaves de fim de curso

import RPi.GPIO as GPIO
import time
import atexit

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
stop = False


led_a = 36
led_b = 38
led_c = 37
led_d = 40
leds = [led_a,led_b,led_c,led_d]
    
botao_a = 29
botao_b = 31
botao_c = 33
botao_d = 35
botoes = [botao_a,botao_b,botao_c,botao_d]

# Valores positivos movem o eixo X passos para a direita e negativos X passos para a esquerda.
def moveAxys(steps):
    
    global currentPosition
    global stop
    
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
        if stop:
            break
        
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

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(botoes, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# LEIA-ME!
# Para testar, descomentar os fors e comentar os whiles.
# Faça o contrário para usar o código

#while(GPIO.input(switchRight)):
for i in range(0,5000): 
    moveAxys(1)

#while(GPIO.input(switchLeft)):
for i in range(0,5000):
    moveAxys(-1);
    axysSize = axysSize + 1

## Loop principal ##

while True:
    
    if (GPIO.input(botao_c))
        stop = True
        GPIO.output(led_c, 1)
        time.sleep(0.1)
        stop = False
    elif (not GPIO.input(botao_c) and GPIO.input(botao_a):
        if currentPosition + 5 >= axysSize:
            GPIO.output(led_c, 1)
        else:
            GPIO.output(led_a, 1)
            moveAxys(5)
    elif (not GPIO.input(botao_c) and GPIO.input(botao_b):
        if currentPosition - 5 >= 0:
            GPIO.output(led_c, 1)
        else:
            GPIO.output(led_b, 1)
            moveAxys(-5)
    
    elif (not GPIO.input(botao_c) and GPIO.input(botao_d):
        goto(0)
    else:
        GPIO.output(leds, 0)
        time.sleep(0.05)
    
    
GPIO.cleanup()
# Para garantir que o motor não vai continuar andando ao terminar a aplicação.
    
def exit_handler():
    print ('Programa encerrado.\n Parando motor.')
    GPIO.cleanup()

atexit.register(exit_handler)    
    
    
