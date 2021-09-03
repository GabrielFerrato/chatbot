#importar bibliotecas necessarias 
import pywhatkit
import keyboard
import time
from datetime import datetime
# Definir para quais contatos vamos testar
contatos = [+'5561983545254', '+5561983856137']
# Intervalo de envio
while len(contatos) >= 1:
    #enviar mensagens
    pywhatkit.sendwhatmsg(contatos[0], 'teste!', datetime.now ().hour, datetime.now().minute + 2)
    del contatos [0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
