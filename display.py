from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
import sys

class Display:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setWindowTitle('Waves')
        self.window.setGeometry(100, 100, 280, 80)
        self.window.move(60, 15)
        
        helloMsg = QLabel('<h1>Hello World!</h1>', parent=self.window)
        helloMsg.move(60, 15)
        
    def show(self):
        # Show window and loop to keep displaying
        self.window.show()
        sys.exit(self.app.exec_())