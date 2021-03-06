import discord
import RPi.GPIO as GPIO
import time
from time import sleep

TOKEN = ''

# Definindo as opçoes da placa

GPIO.setwarnings(False) # Desabilita uma interrupcao por causa de um "Warning"
GPIO.setmode(GPIO.BOARD) # Definindo a orientaçao dos pinos


# Definindo pinos de saída e entrada

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

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'hello, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!seq1'):
        GPIO.output(led_azul,1)
        time.sleep(1)
        GPIO.output(led_azul,0)
    if message.content.startswith('!seq2'):
        for x in range(10):
            GPIO.output(leds,1)
            time.sleep(0.5)
            GPIO.output(leds,0)
            time.sleep(0.5)

    if message.content.startswith('!seq3'):
        None
    if message.content.startswith('!desliga'):
        None



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
