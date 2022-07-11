#importamos librerias
import pywhatkit

from datetime import datetime
import time

#Enviar un mensaje en cierto tiempo
#seconds = time.time()+60
#date = datetime.fromtimestamp(seconds)


pywhatkit.sendwhatmsg("+593992096010",
                            "Hola",
                            22,
                            12, 
                            )
time.sleep(5)