import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint

def lerMensagem(message):
    # Dando uma olhada rápida na mensagem que chegou e atribuindo as 3 variáveis.
    content_type, chat_type, chat_id = telepot.glance(message)
    
    # Checa se a mensagem é do tipo texto
    if content_type == 'text':
        # Envia a mensagem que o usuário acabou de mandar
        meuBot.sendMessage(chat_id, message['text'])


meuBot = telepot.Bot('insira a token aqui')
MessageLoop(meuBot, lerMensagem).run_as_thread()
print("Bot ligado")

while (True):
    time.sleep(1)

