import websocket
from threading import Thread, Timer
import json
import access_codes
import time
import socket

class Twin_Sub(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.client_id, self.token, self.secret = access_codes.app_codes()
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #self.serversocket.connect(('192.168.0.6', 3232))
        self.serversocket.connect(('192.168.1.195', 3232))
    
    def run(self):
        self.ws = websocket.WebSocketApp("wss://pubsub-edge.twitch.tv",
                                        on_message = self.on_message,
                                        on_open = self.on_open)
        self.ws.run_forever()

    def pinger(self):
        message = {
            "type" : "PING"
        }
        self.ws.send(json.dumps(message))

    def on_message(self, message):
        value = json.loads(message)
        try:
            final_value = json.loads(value["data"]["message"])
            self.handler(final_value["data"]["redemption"]["reward"]["title"])
        except:
            pass

    def on_open(self):
        message = {
            "type": "LISTEN",
            "data": {
                "topics": ["channel-points-channel-v1.153781693"],
                "auth_token": self.token
            }
        }
        self.ws.send(json.dumps(message))
        self.TimerPing(250, self.pinger).start()

    def handler(self, message):
        message = message.lower()
        if message == "zap both":
            self.serversocket.send(b'zap')
        elif message == "zap cade":
            self.serversocket.send(b'zap cade')
        elif message == "zap brandt":
            self.serversocket.send(b'zap brandt')
        elif message == "make twins drink":
            self.serversocket.send(b'drink')
        elif message == "make cade drink":
            self.serversocket.send(b'drink cade')
        elif message == "make brandt drink":
            self.serversocket.send(b'drink brandt')

    class TimerPing(Timer):
        def __init__(self, time, func):
            Timer.__init__(self, time, func)
            self.running = True

        def run(self):
            while(self.running):
                self.finished.wait(self.interval)
                if not self.finished.is_set():
                    self.function(*self.args, **self.kwargs)
                self.finished.clear()   
        
        @property
        def stop_timer(self):
            self.finished.set()
            self.running = False

if __name__ == "__main__":
    TS = Twin_Sub()
    TS.start()