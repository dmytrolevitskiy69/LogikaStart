from PyQt5.QtWidgets import QApplication, QWidget
from main_window import*


app = QApplication([])
window_width = 650
window_height = 500
question_window = QWidget()
question_window.resize(window_height, window_width)
question_window.move(300,300)
question_window.setWindowTitle("Memory Card")

question_window.setLayout(main_v_layout)

question_window.show()
app.exec_()