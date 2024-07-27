from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, 
                            QSpinBox, QPushButton, QGroupBox, QButtonGroup)

btn_menu = QPushButton("Меню")
btn_relax = QPushButton('Відпочити')
spb_timer = QSpinBox()
spb_timer.setValue(30)
lb_timer = QLabel("хвилин")
lb_quest = QLabel('')

RadioGroupBox = QGroupBox('Варіанти відповідей') #для рамки
RadioGroup = QButtonGroup()

rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('') 
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

AnswerBox = QGroupBox("Результат теста")
lb_result = QLabel('') #Правильно/неправильно
lb_correct = QLabel('') # Правильна відповідь

btn_ok = QPushButton()

v_layout_ans_1 = QVBoxLayout()
v_layout_ans_2 = QVBoxLayout()
h_layout_ans_3 = QHBoxLayout()

v_layout_ans_1.addWidget(rbtn_1)
v_layout_ans_1.addWidget(rbtn_2)
v_layout_ans_2.addWidget(rbtn_3)
v_layout_ans_2.addWidget(rbtn_4)

h_layout_ans_3.addLayout(v_layout_ans_1)
h_layout_ans_3.addLayout(v_layout_ans_2)

RadioGroupBox.setLayout(h_layout_ans_3)

v_layout_res = QVBoxLayout()
v_layout_res.addWidget(lb_result, alignment=Qt.AlignLeft | Qt.AlignTop)
v_layout_res.addWidget(lb_correct, alignment=Qt.AlignCenter)
AnswerBox.setLayout(v_layout_res)
AnswerBox.hide()

h_layout_1 = QHBoxLayout()
h_layout_2 = QHBoxLayout()
h_layout_3 = QHBoxLayout()
h_layout_4 = QHBoxLayout()

h_layout_1.addWidget(btn_menu)
h_layout_1.addStretch(1)
h_layout_1.addWidget(btn_relax)
h_layout_1.addWidget(spb_timer)
h_layout_1.addWidget(lb_timer)

h_layout_2.addWidget(lb_quest, alignment=Qt.AlignHCenter)

h_layout_3.addWidget(RadioGroupBox)
h_layout_3.addWidget(AnswerBox)

h_layout_4.addStretch(1)
h_layout_4.addWidget(btn_ok, stretch=2)
h_layout_4.addStretch(1)

main_v_layout = QVBoxLayout()
main_v_layout.addLayout(h_layout_1, stretch=1)
main_v_layout.addLayout(h_layout_2, stretch=2)
main_v_layout.addLayout(h_layout_3, stretch=8)
main_v_layout.addStretch(1)
main_v_layout.addLayout(h_layout_4, stretch=1)
main_v_layout.addStretch(1)
# main_v_layout.setSpacing(5)

