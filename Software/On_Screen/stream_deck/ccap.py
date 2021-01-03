import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversocket.connect(('192.168.0.64', 3232))
serversocket.send(b'forward')