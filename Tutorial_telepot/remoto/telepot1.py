import time
from time import sleep
import random
import datetime
import telepot
import RPi.GPIO as GPIO


# Definindo as opçoes da placa

GPIO.setwarnings(False) # Desabilita uma interrupcao por causa de um "Warning"
GPIO.setmode(GPIO.BOARD) # Definindo a orientaçao dos pinos


# Definindo pinos de saída e entrada

led_verde = 36
led_amarelo = 37
led_vermelho = 38
led_azul = 40
leds = [led_verde,led_amarelo,led_vermelho,led_azul]

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds,0)

botao_verde = 29
botao_amarelo = 31
botao_vermelho = 33
botao_azul = 35
botoes = [botao_verde,botao_amarelo,botao_vermelho,botao_azul]

GPIO.setup(botoes, GPIO.IN, pull_up_down=GPIO.PUD_UP)


for x in leds:
    GPIO.setup(x,GPIO.OUT)
    GPIO.output(x,0)


for x in botoes:
    GPIO.setup(x,GPIO.IN,GPIO.PUD_UP)



def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    nome = msg['chat']['first_name']

    print ('Qual comando: %s' % command)
    print ("Quem mandou: %s" % nome)

    if command == '/comandos' or command == '/start':
        bot.sendMessage(chat_id, "Lista de comandos: /liga\n/desliga\n/seq1\n/seq2\n/seq3\n/but1\n/but2")
    elif command == '/start':
        bot.sendMessage(chat_id,"Bom dia, boa tarde e boa noite")
    elif command == '/liga':
        GPIO.output(led_azul,1)
    elif command == '/desliga':
        GPIO.output(led_azul,0)
    elif command == '/seq1':
        for x in leds:
            GPIO.output(x,1)
            sleep(0.3)
        for x in leds:
            GPIO.output(x,0)
            sleep(0.3)

    elif command == '/seq2':
        GPIO.output(led_azul,1)
    elif command == '/seq3':
        GPIO.output(leds,1)
    elif command == '/but1':
        for x in range(50):
            GPIO.output(leds,1)
            sleep(0.2)
            GPIO.output(leds,0)
            sleep(0.2)
    elif command == '/but1':
        GPIO.output(led_azul,1)
    elif command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/random':
       for x in leds:
           GPIO.output(x,random.randint(0,1))
           sleep(0.5)

bot = telepot.Bot('')
bot.message_loop(handle)
print ('I am listening ...')

while 1:
    time.sleep(10)
