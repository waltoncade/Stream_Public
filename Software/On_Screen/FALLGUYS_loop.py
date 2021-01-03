import Computervision
import time
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#serversocket.connect(('192.168.0.6', 3232))
serversocket.connect(('192.168.1.195', 3232))
fgobject = Computervision.fallguyscv()

while True:
    fgobject.iseliminated()
    fgobject.isqualified()
    if fgobject.lose:
        serversocket.send(b'zap')
        time.sleep(10)
    if fgobject.win:
        time.sleep(2)
        serversocket.send(b'drink')
        serversocket.send(b'drink')
        serversocket.send(b'drink')
        time.sleep(10)
    time.sleep(0.5)