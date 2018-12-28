# Autor: Pedro Vinicius Custodio
## Código para usar o módulo A4988 e 2 chaves de fim de curso

import RPi.GPIO as GPIO
import time
import atexit
import Eixo

# Usando a FakeRPiGPIO para testar o código. Remover próxima linha para usar na RaspberryPi | $ pip install fakeRPiGPIO
GPIO.VERBOSE = False

# Os pinos usados. Troque se quiser
direction = 11
step = 13
enable = 15

# Chaves de fim de curso
switchLeft = 23
switchRight = 24

# Leds indicadores
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

# Início do programa

GPIO.setmode(GPIO.BOARD)

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(botoes, GPIO.IN, pull_up_down=GPIO.PUD_UP)


## Loop principal ##

Eixo.init()

while True:
    
    if (not GPIO.input(botao_c)):
        stop = True
        GPIO.output(led_c, 1)
        time.sleep(0.1)
        stop = False
    elif (GPIO.input(botao_c) and not GPIO.input(botao_a)):
        if Eixo.currentPosition + 5 >= Eixo.axysSize:
            GPIO.output(led_c, 1)
        else:
            GPIO.output(led_a, 1)
            Eixo.moveAxys(5)
    elif (GPIO.input(botao_c) and not GPIO.input(botao_b)):
        if Eixo.currentPosition - 5 >= 0:
            GPIO.output(led_c, 1)
        else:
            GPIO.output(led_b, 1)
            Eixo.moveAxys(-5)
    
    elif (GPIO.input(botao_c) and not GPIO.input(botao_d)):
        Eixo.goto(0)
    else:
        GPIO.output(leds, 0)
        time.sleep(0.05)
    
    
GPIO.cleanup()
# Para garantir que o motor não vai continuar andando ao terminar a aplicação.
    
def exit_handler():
    print ('Programa encerrado.\n Parando motor.')
    GPIO.cleanup()

atexit.register(exit_handler)    
    
    
