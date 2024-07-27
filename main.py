from PyQt5.QtWidgets import QApplication, QWidget
from random import choice, shuffle
from time import sleep

app = QApplication([])

from main_window import*
from menu_window import*

class Question():
    def __init__(self, question, cor_unswer, wrong_unswer1,wrong_unswer2, wrong_unswer3):
        self.question = question
        self.answer = cor_unswer
        self.wrong_answer1 = wrong_unswer1
        self.wrong_answer2 = wrong_unswer2
        self.wrong_answer3 = wrong_unswer3
        self.attempts = 0
        self.correct = 0
    
    def got_right(self):
        self.attempts += 1
        self.correct += 1
        # print('Це правильна відповідь!')

    def got_wrong(self):
        self.attempts += 1
        # print("Відповідь невірна")


q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

questions = [q1, q2, q3, q4]
random_question = choice(questions)
# print(random_question)
def clear_rbnt():
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_question(current_question):
    clear_rbnt()
    
    AnswerBox.hide()
    RadioGroupBox.show()
    
    lb_quest.setText(current_question.question)
    
    radio_list = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
    shuffle(radio_list)

    global answer
    answer = radio_list[0]
    wrong_answer1 = radio_list[1]
    wrong_answer2 = radio_list[2]
    wrong_answer3 = radio_list[3]

    answer.setText(current_question.answer)
    wrong_answer1.setText(current_question.wrong_answer1)
    wrong_answer2.setText(current_question.wrong_answer2)
    wrong_answer3.setText(current_question.wrong_answer3)

    btn_ok.setText('Відповісти')

def check_answer():
    RadioGroupBox.hide()
    AnswerBox.show()
    btn_ok.setText('Наступне')

    if  answer.isChecked():
        lb_result.setText('Відповідь вірна!')
        lb_correct.setText(answer.text())
        got_right()
    else:
        lb_result.setText('Відповідь НЕ вірна!')
        lb_correct.setText(answer.text())
        got_wrong()

def click_OK():
    if btn_ok.text() == 'Відповісти':
        check_answer()
    else:
        random_question = choice(questions)
        show_question(random_question)

def rest():
    t = spb_timer.value()
    question_window.hide()
    sleep(t)
    question_window.show()

def got_right():
    global attempts, correct
    attempts += 1
    correct += 1

def got_wrong():
    global attempts
    attempts += 1

def stat():
    global attempts, correct
    try:
        success = correct/attempts * 100
    except:
        success = 0
    return round(success, 2)

def menu():
    global attempts, correct
    question_window.hide()
    lb_atte.setText("Разів відповіли:" + str(attempts))
    lb_cor.setText("Вірно відповіли:" + str(correct))
    lb_success.setText("Успішність:" + str(stat()) + '%')
    menu_window.show()

def back():
    menu_window.hide()
    question_window.show()

def clear_le():
    le_quest.clear()
    le_cor_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()

def add_quest():
    global questions
    q = Question(le_quest.text(), le_cor_ans.text(),
                 le_wrong_ans1.text(), le_wrong_ans2.text(), le_wrong_ans3.text())
    questions.append(q)

def next_quest():
    global num
    num += 1
    edit_quest()
    
def prew_quest():
    global num
    num -= 1
    edit_quest()

def edit_quest():
    global questions, num

    current_quest = questions[num % len(questions)]
    le_quest.setText(current_quest.question)
    le_cor_ans.setText(current_quest.answer)
    le_wrong_ans1.setText(current_quest.wrong_answer1)
    le_wrong_ans2.setText(current_quest.wrong_answer2)
    le_wrong_ans3.setText(current_quest.wrong_answer3)

attempts = 0
correct = 0
num = 0

window_width = 650
window_height = 500

#######################################3

question_window = QWidget()
question_window.resize(window_width,window_height)
question_window.move(300,300)
question_window.setWindowTitle("Memory Card")
question_window.setLayout(main_v_layout)
show_question(random_question)
btn_ok.clicked.connect(click_OK)
btn_relax.clicked.connect(rest)
btn_menu.clicked.connect(menu)

question_window.show()

##############################################3

menu_window = QWidget()

menu_window.resize(window_width,window_height)
menu_window.move(300,300)
menu_window.setWindowTitle("Menu")
menu_window.setLayout(v_menu_layout)

btn_back.clicked.connect(back)
btn_clear.clicked.connect(clear_le)
btn_add.clicked.connect(add_quest)
btn_next.clicked.connect(next_quest)
btn_prew.clicked.connect(prew_quest)

menu_window.hide()

################################################

app.exec_()