import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint

# Criando uma função para ler as mensagens
def lerMensagem(message):
    pprint(message)

# Aossiciando uma váriavel do tipo bot
meuBot = telepot.Bot('insira a token aqui')

# Rodando o Loop de leitura de mensagens
MessageLoop(meuBot, lerMensagem).run_as_thread()

# Indicando que o bot ligou
print("Bot ligado")

# Deixando ele ligado
while (True):
    time.sleep(1)
