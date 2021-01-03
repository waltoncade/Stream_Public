import Computervision
import time
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#serversocket.connect(('192.168.0.6', 3232))
serversocket.connect(('192.168.1.195', 3232))
auobject = Computervision.amonguscv()

while True:
    auobject.whichteam()
    if auobject.lightstate():
        print('sent')
        if auobject.lights:
            serversocket.send(b'lightsoff')
        else:
            serversocket.send(b'lightson')
    if auobject.ingame:
        auobject.isreported()
        auobject.iscracked()
        if not auobject.reported and auobject.crack and auobject.crewmate:
            #serversocket.send(b'zap')
            time.sleep(6)
    print("Imposter Record: " + str(auobject.imposterwins) + "/" + str(auobject.imposterloses))
    print("Crewmate Record: " + str(auobject.crewmatewins) + "/" + str(auobject.crewmateloses) + '\n')