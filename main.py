#!/usr/bin/python3

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUiType
import sys
from main_ui import Ui_MainWindow
import time

#MainUI, _ = loadUiType('main.ui')

counter = 0

class Main(QMainWindow , Ui_MainWindow):
    def __init__(self , parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.progress()

        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint)
        self.prog.setMaximum(100)
        self.prog.setValue(0)

        timer = QTimer(self)
        timer.timeout.connect(self.progress)
        timer.start(50)

    def progress(self):
        self.prog.setValue(self.prog.value() + 1)
        while self.prog.value() == 100 :
            self.close()
            sys.exit()
        


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
