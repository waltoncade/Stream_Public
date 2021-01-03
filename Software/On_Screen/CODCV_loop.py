import Computervision
import time
import socket
import numpy as np

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#serversocket.connect(('192.168.0.6', 3232))
serversocket.connect(('192.168.1.195', 3232))
codobject = Computervision.codcv()
prevkill = 0

while True:    
    codobject.isspectating()
    codobject.isingame()
    if codobject.startgame and not codobject.spectating:
        codobject.isdead()
        codobject.iskill()
        if codobject.confirm_kill > prevkill and codobject.confirm_kill != -1:
            sendstring = "CV:KILL:{}".format(codobject.confirm_kill - prevkill)
            serversocket.send(bytes(sendstring, "utf-8"))
            prevkill = codobject.confirm_kill
    
    if codobject.confirm_kill == 0:
        prevkill = 0
        killchecker = 0

    if codobject.dead:
        serversocket.send(b'death')
        time.sleep(5)
    
    if codobject.startflag:
        time.sleep(65)
        codobject.startflag = False

    print('kills: ' + str(codobject.confirm_kill) + '   dead: ' + str(codobject.dead) + '   ingame: ' + str(codobject.startgame) + '  spectating: ' + str(codobject.spectating))
    