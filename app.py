import pywhatkit
import keyboard
import time
from datetime import datetime

contatos = [+'5561983545254', '+5561983856137']
 
while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0], 'oi!', )