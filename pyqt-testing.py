from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
my_win = QWidget()

text = QLabel("Натисніть, щоб дізнатися переможця")
winner = QLabel("?")
button = QPushButton("Згенерувати")

line = QVBoxLayout()
line.addWidget(text)
line.addWidget(winner)
line.addWidget(button)
my_win.setLayout(line)

def show_winner():
    num = randint(1,100)
    winner.setText(str(num))
    text.setText("Переможець:")
button.clicked.connect(show_winner)

my_win.show()
app.exec()