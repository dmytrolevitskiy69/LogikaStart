from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QMessageBox

def uncor():
    mess = QMessageBox()
    mess.setText("Ні, в 2015 році. Ви виграли фірмовий плакат")
    mess.exec_()

def cor():
    pas = QMessageBox()
    pas.setText("Правильно! Ви виграли гіроскутер")
    pas.exec_()

app = QApplication([])
window = QWidget()
window.resize(400,200)
window.setWindowTitle('Конкурс від Crazy People')

question = QLabel("В якому році канал отримав 'золоту кнопку' від YouTube?")
rbtn_1 = QRadioButton("2005")
rbtn_2 = QRadioButton("2010")
rbtn_3 = QRadioButton("2015")
rbtn_4 = QRadioButton("2020")

v_line = QVBoxLayout()
h_line_1 = QHBoxLayout()
h_line_2 = QHBoxLayout()
h_line_3 = QHBoxLayout()

h_line_1.addWidget(question, alignment=Qt.AlignCenter)
h_line_2.addWidget(rbtn_1, alignment=Qt.AlignCenter)
h_line_2.addWidget(rbtn_2, alignment=Qt.AlignCenter)
h_line_3.addWidget(rbtn_3, alignment=Qt.AlignCenter)
h_line_3.addWidget(rbtn_4, alignment=Qt.AlignCenter)

v_line.addLayout(h_line_1)
v_line.addLayout(h_line_2)
v_line.addLayout(h_line_3)
window.setLayout(v_line)

rbtn_1.clicked.connect(uncor)
rbtn_2.clicked.connect(uncor)
rbtn_3.clicked.connect(cor)
rbtn_4.clicked.connect(uncor)



window.show()
app.exec_()
