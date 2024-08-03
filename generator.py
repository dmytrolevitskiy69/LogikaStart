import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QLinearGradient, QBrush
import random
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui',self)
        #self.dolar.clicked.connect(self.dollars)
        self.btn_generator.clicked.connect(self.parol)
        

    def parol(self):
        symbol = ''
        if self.ch8_number.isChecked():
            symbol += '0123456789'
        if self.ch8_alph.isChecked():
            symbol += 'qwertyuiopasdfghjklzxcvbnm'
        
        result = ''
        len_of_pas = random.randint(8,16)
        for i in range(len_of_pas):
            result += random.choice(symbol)
        
        self.lb_result.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())