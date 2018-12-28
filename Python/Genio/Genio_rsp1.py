import RPi.GPIO as GPIO
from time import sleep
from random import randint

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led_a = 11
led_b = 13
led_c = 15
led_d = 16
leds = [led_a,led_b,led_c,led_d]

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds,0)

botao_a = 3
botao_b = 5
botao_c = 7
botao_d = 8
botoes = [botao_a,botao_b,botao_c,botao_d]

GPIO.setup(botoes, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Criando lista vazia
sequencia = []

while True:

    # Criando uma sequência aleatória a cada loop
    novo = randint(0,3)
    sequencia.append(novo)

    # Mostrando qual botão deve ser apertado em seguida
    for x in sequencia:
        GPIO.output(leds[x], GPIO.HIGH)
        sleep(1.8)
        GPIO.output(leds[x], GPIO.LOW)
        sleep(0.2)

    for x in sequencia:
        # Foi o melhor jeito que pensei pra evitar ganhar o jogo apertando todos os botões.
        # A tabela verdade mostrará a verdade.

        soma = 0
        trava = 0

        while(soma == 0):
            valor_botao_a = (not GPIO.input(botao_a))*1
            valor_botao_b = (not GPIO.input(botao_b))*2
            valor_botao_c = (not GPIO.input(botao_c))*4
            valor_botao_d = (not GPIO.input(botao_d))*8
            soma = valor_botao_a + valor_botao_b + valor_botao_c + valor_botao_d
            trava = soma

            sleep(0.05)
            continue # Continua no loop

        while(soma == trava):
            valor_botao_a = (not GPIO.input(botao_a))*1
            valor_botao_b = (not GPIO.input(botao_b))*2
            valor_botao_c = (not GPIO.input(botao_c))*4
            valor_botao_d = (not GPIO.input(botao_d))*8
            trava = valor_botao_a + valor_botao_b + valor_botao_c + valor_botao_d

            sleep(0.05)
            continue # Continua no loop



        print (soma)

        # Se você acertou qual era o botão
        if soma == 2**x:
            # Faz um showzinho pra mostrar que acertou.
            for x in leds:
                GPIO.output(x, GPIO.HIGH)
                sleep(0.1)
                GPIO.output(x, GPIO.LOW)
            sleep(0.2)
            continue
        else:
            # É isso mesmo
            print ('Você perdeu!\nReiniciando o jogo...')
            for x in range(0,4):
                GPIO.output(leds,GPIO.HIGH)
                sleep(0.25)
                GPIO.output(leds,GPIO.LOW)
                sleep(0.25)
            print("Você acertou %d vezes!\n "% (int(len(sequencia))-1))
            sequencia = []
            break
