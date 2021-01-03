from PyQt5 import QtCore, QtWidgets, QtGui, Qt, uic

class App(QtWidgets.QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Split-Stream'
        self.left = 500
        self.top = 900
        self.width = 1200
        self.height = 150
        self.center = self.width/2
        self.filepath = "C:/Git/Stream/Software/On_Screen/"
        self.initUI()
         
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.palette = QtGui.QPalette()
        self.palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)

        self.timer_l = 30

        #pictures========================================================

        #background
        self.background = QtWidgets.QLabel(self)
        self.background.setPixmap(QtGui.QPixmap('{}/pictures/UI/grey.png'.format(self.filepath)))
        self.background.move(0, 0)
        self.background.resize(1200, 700)

        #right arrow
        self.right_arrow = QtWidgets.QLabel(self)
        self.right_arrow.setPixmap(QtGui.QPixmap('{}/pictures/UI/Red_Right.png'.format(self.filepath)))
        self.right_arrow.move(self.center + 30, 0)
        self.right_arrow.resize(185, 157)

        #left arrow
        self.left_arrow = QtWidgets.QLabel(self)
        self.left_arrow.setPixmap(QtGui.QPixmap('{}/pictures/UI/Red_Left.png'.format(self.filepath)))
        self.left_arrow.move(self.center - 295, 0)
        self.left_arrow.resize(185, 157)

        #labels==========================================================

        #commands
        self.label = QtWidgets.QLabel(self)
        self.label.setText("cool")
        self.label.setGeometry(QtCore.QRect(self.center + 320, 280, 150, 16))

        #Who's Playing?
        self.playing = QtWidgets.QLabel(self)
        #self.playing.setText("Who's Playing?")
        self.playing.setGeometry(QtCore.QRect(self.center - 95, 125, 300, 60))
        self.playing.setFont(QtGui.QFont('Times', 18, QtGui.QFont.Bold, True))

        #Timer
        self.timer = QtWidgets.QLabel(self)
        self.timer.setText('{}:{:02d}'.format(0,self.timer_l))
        self.timer.setGeometry(QtCore.QRect(self.center - 130, -175, 2000, 500))
        self.timer.setFont(QtGui.QFont('Times', 60, QtGui.QFont.Bold, False))

        #Right_Counter
        self.cade_count = QtWidgets.QLabel(self)
        self.cade_count.setText('0')
        self.cade_count.setGeometry(QtCore.QRect(self.center + 250, 20, 400, 100))
        self.cade_count.setFont(QtGui.QFont('Times', 60, QtGui.QFont.Bold, False))
        
        #Left Counter
        self.brandt_count = QtWidgets.QLabel(self)
        self.brandt_count.setText('0')
        self.brandt_count.setGeometry(QtCore.QRect(self.center - 550, 20, 400, 100))
        self.brandt_count.setFont(QtGui.QFont('Times', 60, QtGui.QFont.Bold, False))

        #call============================================================
        self.show()