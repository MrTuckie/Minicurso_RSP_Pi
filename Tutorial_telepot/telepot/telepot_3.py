import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint
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

botao_verde = 29
botao_amarelo = 31
botao_vermelho = 33
botao_azul = 35
botoes = [botao_verde,botao_amarelo,botao_vermelho,botao_azul]

for x in leds:
    GPIO.setup(x,GPIO.OUT)
    GPIO.output(x,0)


for x in botoes:
    GPIO.setup(x,GPIO.IN,GPIO.PUD_UP)


def lerMensagem(message):
    # Dando uma olhada rápida na mensagem que chegou e atribuindo as 3 variáveis.
    content_type, chat_type, chat_id = telepot.glance(message)
    
    # Checa se a mensagem é do tipo texto
    if content_type == 'text':
        #Checa se a mensagem é igual a /comandos
        if message['text'] == '/comandos':
            meuBot.sendMessage(chat_id, "Lista de comandos: /amarelo\n/azul\n/verde\n/vermelho")
            
        if (message['text'] == '/azul'):
           print("Piscando o led azul!")
           meuBot.sendMessage(chat_id, "Piscando led azul!")
           for x in range (3):
               GPIO.output(led_azul,1)
               time.sleep(1)
               GPIO.output(led_azul,0)
               time.sleep(1)
               
        if (message['text'] == '/vermelho'):
           print("Piscando o led vermelho!")
           meuBot.sendMessage(chat_id, "Piscando led vermelho!")
           for x in range (3):
               GPIO.output(led_vermelho,1)
               time.sleep(1)
               GPIO.output(led_vermelho,0)
               time.sleep(1)
               
        if (message['text'] == '/verde'):
           print("Piscando o led verde!")
           meuBot.sendMessage(chat_id, "Piscando led verde!")
           for x in range (3):
               GPIO.output(led_verde,1)
               time.sleep(1)
               GPIO.output(led_verde,0)
               time.sleep(1)
               
        if (message['text'] == '/amarelo'):
           print("Piscando o led amarelo!")
           meuBot.sendMessage(chat_id, "Piscando led amarelo!")
           for x in range (3):
               GPIO.output(led_amarelo,1)
               time.sleep(1)
               GPIO.output(led_amarelo,0)
               time.sleep(1)
    
        

meuBot = telepot.Bot('insira a token aqui')
MessageLoop(meuBot, lerMensagem).run_as_thread()
print("Bot ligado")

while (True):
    time.sleep(1)


