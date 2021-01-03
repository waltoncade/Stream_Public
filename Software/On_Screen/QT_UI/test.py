from PyQt5 import QtWidgets, uic
import sys

filepath = "C:/Git/Stream/Software/On_Screen/QT_UI/"

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(filepath + 'main.ui', self) # Load the .ui file
        self.show() # Show the GUI

app = QtWidgets.QApplication(sys.argv)
ex = Ui()

c = input()