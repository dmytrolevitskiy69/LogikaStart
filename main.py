from PyQt5.QtWidgets import QApplication, QWidget
from random import choice, shuffle

app = QApplication([])
from main_window import*

class Question():
    def __init__ (self, question, answer, wrong_answer, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer = wrong_answer
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.attempts = 0
        self.correct = 0

    def got_right(self):    
        self.attempts += 1
        self.correct += 1
        #print("Це правильна відповідь!")

    def got_wrong(self):
        self.attempts +=1
        #print("Відповідь невірна.")

def show_question(random_question):
    rbtn_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
    shuffle(rbtn_list)

    answer = rbtn_list[0]
    wrong_answer = rbtn_list[1]
    wrong_answer2 = rbtn_list[2]
    wrong_answer3 = rbtn_list[3]

    lb_quest.setText(random_question.question)
    answer.setText(random_question.answer)
    wrong_answer.setText(random_question.wrong_answer)
    wrong_answer2.setText(random_question.wrong_answer2)
    wrong_answer3.setText(random_question.wrong_answer3)

    btn_ok.setText("Відповісти")

def click_OK():
    pass

q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

questions = [q1, q2, q3, q4]
random_question = choice(questions)

window_width = 650
window_height = 500
question_window = QWidget()
question_window.resize(window_width,window_height)
question_window.move(300,300)
question_window.setWindowTitle("Memory Card")

question_window.setLayout(main_v_layout)


show_question(random_question)
btn_ok.clicked.connect(click_OK)

question_window.show()
app.exec_()