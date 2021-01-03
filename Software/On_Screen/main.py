import serial, sys, os
import datetime, time
import threading
import socket
import shutil
from PyQt5 import QtCore, QtWidgets, QtGui, Qt, uic
from ui import App
from pynput.keyboard import Key, Controller
from pubsub import Twin_Sub

ser = serial.Serial('com4', 9600)
filepath = "C:/Git/Stream/Software/On_Screen/"
cade_kills = 0.0
brandt_kills = 0.0
cade_deaths = 0.0
brandt_deaths = 0.0
keyboard = Controller()

def swap(name, color):
    os.remove("{}/pictures/UI/{}.jpg".format(filepath,name))
    shutil.copy("{}/pictures/UI/{}.jpg".format(filepath,color), "{}/pictures/UI/{}.jpg".format(filepath,name))

def serial_receive(ui,num):
    global clock
    while True:
        if (ser.inWaiting()>0):
            data = ser.readline()
            data = data[0:-2]
            ui.label.setText('{}'.format(data))
            if (data == b'Player 1'):
                pic1_switch = threading.Thread(target=swap, args=('cade','green'))
                pic2_switch = threading.Thread(target=swap, args=('brandt','red'))
                pic1_switch.start()
                pic2_switch.start()
                ui.left_arrow.setPixmap(QtGui.QPixmap('{}/pictures/UI/Red_Left.png'.format(filepath)))
                ui.right_arrow.setPixmap(QtGui.QPixmap('{}/pictures/UI/Green_Right.png'.format(filepath)))
            if (data == b'Player 2'):
                pic1_switch = threading.Thread(target=swap, args=('cade','red'))
                pic2_switch = threading.Thread(target=swap, args=('brandt','green'))
                pic1_switch.start()
                pic2_switch.start()
                ui.left_arrow.setPixmap(QtGui.QPixmap('{}/pictures/UI/Green_Left.png'.format(filepath)))
                ui.right_arrow.setPixmap(QtGui.QPixmap('{}/pictures/UI/Red_Right.png'.format(filepath)))
            if (data == b'Player Transition'):
                ui.left_arrow.setPixmap(QtGui.QPixmap('{}/pictures/UI/Yellow_Left.png'.format(filepath)))
                ui.right_arrow.setPixmap(QtGui.QPixmap('{}/pictures/UI/Yellow_Right.png'.format(filepath)))
            if (data == b'shock1'):
                graphic('cade')
            elif (data == b'shock2'):
                graphic('brandt')
            elif (data == b'shockboth'):
                graphic('both')

        try:
            brandt_kd = brandt_kills/brandt_deaths
            cade_kd = cade_kills/cade_deaths
        except:
            brandt_kd = brandt_kills/1.0
            cade_kd = cade_kills/1.0

        ui.timer.setText('{}:{:02d}'.format(0,clock))
        ui.brandt_count.setText('{:.2f}'.format(brandt_kd))
        ui.cade_count.setText('{:.2f}'.format(cade_kd))
        time.sleep(0.01)

def timer():
    global clock
    global decrement
    global next_player
    clock = 30
    decrement = 1
    time.sleep(2)
    next_player = "Brandt"
    ser.write(b"CCr")
    while True:
        time.sleep(1)
        clock -= decrement
        if clock == 2 and next_player == "Cade":
            ser.write(b"CCr")
            next_player = "Brandt"
        elif clock == 2 and next_player == "Brandt":
            ser.write(b"BCr")
            next_player = "Cade"
        elif clock == 0:
            clock = 30

def socket_recieve():
    global clock
    global decrement
    global next_player
    global shock
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #serversocket.bind(('192.168.0.6', 3232))
    serversocket.bind(('192.168.1.195', 3232))
    while True:
        data, addr = serversocket.recvfrom(1024)
        msg = data.decode("utf-8")
        if msg == "death":
            cv(msg)
        elif msg == "cade_perm":
            ser.write(b"CCr")
            clock = 30
            decrement = 0
        elif msg == "brandt_perm":
            ser.write(b"BCr")
            clock = 30
            decrement = 0
        elif msg == "cade":
            clock = 30
            ser.write(b"CCr")
            next_player = "Brandt"
            decrement = 1
        elif msg == "brandt":
            clock = 30
            ser.write(b"BCr")
            next_player = "Cade"
            decrement = 1
        elif msg == "drink":
            ser.write(b"TDr")
        elif msg == "drink cade":
            ser.write(b"CDr")
        elif msg == "drink brandt":
            ser.write(b"BDr")
        elif msg == "zap":
            ser.write(b"TZr")
        elif msg == "zap cade":
            ser.write(b"CZr")
        elif msg == "zap brandt":
            ser.write(b"BZr")
        elif msg == "cookie":
            graphic('cookie')
        elif msg == "lightsoff":
            graphic('lightsoff')
        elif msg == "lightson":
            graphic('lightson')
        elif "WEB_FOLLOW:" in msg:
            print(msg[11:])
            graphic('both')
            ser.write(b"TZr")
        elif "CV:" in msg:
            cv(msg[3:])
        time.sleep(0.01)

def cv(data):
    global next_player
    global cade_kills
    global brandt_kills
    global brandt_deaths
    global cade_deaths
    print(data)
    if "KILL" in data:
        try:
            data = int(data[5:])
            if next_player == "Cade":
                brandt_kills += data
            if next_player == "Brandt":
                cade_kills += data
        except:
            print("no work")
    if data == 'death':
        #ser.write(b'Z')
        if next_player == "Cade":
            brandt_deaths += 1.0
        if next_player == "Brandt":
            cade_deaths += 1.0

def graphic(name):
    if name == 'both':
        keyboard.press(Key.ctrl)
        keyboard.press('1')
        keyboard.press('2')
        time.sleep(0.1)
        keyboard.release(Key.ctrl)
        keyboard.release('1')
        keyboard.release('2')
    elif name == 'cade':
        keyboard.press(Key.ctrl)
        keyboard.press('2')
        time.sleep(0.1)
        keyboard.release(Key.ctrl)
        keyboard.release('2')
    elif name == 'brandt':
        keyboard.press(Key.ctrl)
        keyboard.press('1')
        time.sleep(0.1)
        keyboard.release(Key.ctrl)
        keyboard.release('1')
    elif name == 'cookie':
        keyboard.press(Key.ctrl)
        keyboard.press('3')
        time.sleep(0.1)
        keyboard.release(Key.ctrl)
        keyboard.release('3')
    elif name == "lightsoff":
        keyboard.press(Key.ctrl)
        keyboard.press('4')
        time.sleep(0.1)
        keyboard.release(Key.ctrl)
        keyboard.release('4')
    elif name == "lightson":
        keyboard.press(Key.ctrl)
        keyboard.press('5')
        time.sleep(0.1)
        keyboard.release(Key.ctrl)
        keyboard.release('5')

def chat_watch(variable):
    import chatbot
    chatbot.main()

def follow_monitor():
    os.system('python {}/webhook_server.py'.format(filepath))
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    TS = Twin_Sub()
    t1 = threading.Thread(target=timer, args=())
    t1.start()
    t3 = threading.Thread(target=socket_recieve, args=())
    t3.start()
    t4 = threading.Thread(target=chat_watch, args=(ex, ))
    t4.start()
    t5 = threading.Thread(target=serial_receive, args=(ex,0,))
    t5.start()
    t6 = threading.Thread(target=follow_monitor, args=())
    t6.start()
    TS.start()
    sys.exit(app.exec_())