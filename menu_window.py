from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QVBoxLayout, QHBoxLayout, 
                            QPushButton, QLineEdit) 
lb_quest_1 = QLabel("Введіть запитання")
lb_cor_ans = QLabel("Введіть вірну відповідь")
lb_wrong_ans1 = QLabel("Введіть першу хибну відповідь")
lb_wrong_ans2 = QLabel("Введіть другу хибну відповідь")
lb_wrong_ans3 = QLabel("Введіть третю хибну відповідь")

le_quest = QLineEdit()
le_cor_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

btn_add = QPushButton("Додати запитання")
btn_clear = QPushButton("Очистити")

lb_stat = QLabel("Статистика:")
lb_atte = QLabel("Разів відповіли:")
lb_cor = QLabel("Вірно відповіли:")
lb_success = QLabel('Успішність:')

btn_prew = QPushButton("Попереднє питання")
btn_next = QPushButton("Наступне питання")

btn_back = QPushButton("Назад")

v_layout_1 = QVBoxLayout()
v_layout_2 = QVBoxLayout()

v_layout_1.addWidget(lb_quest_1)
v_layout_1.addWidget(lb_cor_ans)
v_layout_1.addWidget(lb_wrong_ans1)
v_layout_1.addWidget(lb_wrong_ans2)
v_layout_1.addWidget(lb_wrong_ans3)

v_layout_2.addWidget(le_quest)
v_layout_2.addWidget(le_cor_ans)
v_layout_2.addWidget(le_wrong_ans1)
v_layout_2.addWidget(le_wrong_ans2)
v_layout_2.addWidget(le_wrong_ans3)

h_layout_1 = QHBoxLayout()
h_layout_1.addLayout(v_layout_1)
h_layout_1.addLayout(v_layout_2)

h_layout_2 = QHBoxLayout()
h_layout_2.addWidget(btn_add)
h_layout_2.addWidget(btn_clear)

v_layout_3 = QVBoxLayout()
v_layout_3.addWidget(lb_stat)
v_layout_3.addWidget(lb_atte)
v_layout_3.addWidget(lb_cor)
v_layout_3.addWidget(lb_success)

h_layout_3 = QHBoxLayout()
h_layout_3.addLayout(v_layout_3)
h_layout_3.addWidget(btn_next)
h_layout_3.addWidget(btn_prew)

h_layout_4 = QHBoxLayout()
h_layout_4.addWidget(btn_back)

v_menu_layout = QVBoxLayout()
v_menu_layout.addLayout(h_layout_1)
v_menu_layout.addLayout(h_layout_2)
v_menu_layout.addLayout(h_layout_3)
v_menu_layout.addLayout(h_layout_4)