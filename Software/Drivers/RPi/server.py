import RPi.GPIO as GPIO
import time
import socket

PWM = 12
DIR = 23
EN = 24
count = 0
end = False

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversocket.bind(('192.168.0.82', 3232))

def forward():
    GPIO.output(EN, GPIO.HIGH)
    PWM0 = GPIO.PWM(PWM, 2000)
    PWM0.start(50)
    GPIO.output(DIR, GPIO.LOW)
    time.sleep(3)
    GPIO.output(DIR, GPIO.HIGH)
    GPIO.output(EN, GPIO.LOW)
    PWM0.stop()

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(EN, GPIO.OUT)

GPIO.output(DIR, GPIO.HIGH)
GPIO.output(PWM, GPIO.LOW)

while (not end):
    data, addr = serversocket.recvfrom(1024)
    msg = data.decode("utf-8")
    if (msg == "forward"):
        forward()
        end = True

GPIO.cleanup()