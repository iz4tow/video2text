#from uuid import getnode as get_mac
from getmac import get_mac_address as gma
import base64

#mac = get_mac()
mac=gma()
#mac = 57185452528973

f=open("licenza.bin","wb")
#composizione:
#AAAA-MM-GG HH:MM:SS|uuid_mac|EN|FR|DE|ES
#PER DISABILITARE LINGUA METTERE XX AL POSTO DELLA STESSA
licenza="EN|2029-12-01 20:00:00|"+str(mac)
#licenza=licenza+"\nFR|2029-12-01 20:00:00|"+str(mac)
#licenza=licenza+"\nES|2029-12-01 20:00:00|"+str(mac)
#licenza=licenza+"\nDE|2029-12-01 20:00:00|"+str(mac)



arr=licenza.encode("utf-8")
base64_bytes = base64.b64encode(arr)
base85_bytes = base64.b85encode(base64_bytes)
f.write(base85_bytes)
f.close()
