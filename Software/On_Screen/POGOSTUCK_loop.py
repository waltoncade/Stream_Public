import Computervision
import time
import socket
import cv2

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#serversocket.connect(('192.168.0.6', 3232))
serversocket.connect(('192.168.1.195', 3232))
pogobject = Computervision.pogostuckcv()

while True:
    pogobject.percentage()
    pogobject.furthest()
    if pogobject.percentageint:
        if (pogobject.furthestpercentageint / pogobject.percentageint) == 1:
            print("drink")
    time.sleep(0.1)