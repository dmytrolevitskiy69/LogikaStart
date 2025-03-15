from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from instructions import txt_instruction, txt_test1, txt_test2,txt_test3, txt_sits

age=7
name=" "
p1,p2,p3 = 0,0,0

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        instr = Label(text=txt_instruction,size_hint=(0.9, 0.2), pos_hint={'center_x': 0.5, 'top': 0.9})
        lbl1 = Label(text="Введіть ім'я", size_hint=(0.3,0.1), pos_hint={'x':0.1, 'top': 0.45})
        lbl2 = Label(text="Введіть вік", size_hint=(0.3,0.1), pos_hint={'x':0.1, 'top': 0.6})
        self.in_name=TextInput(multiline=False,size_hint=(0.4,0.1),pos_hint={'x': 0.4, 'top': 0.5})
        self.in_age=TextInput(multiline=False,size_hint=(0.4,0.1),pos_hint={'x': 0.4, 'top': 0.6})
        self.btn=Button(text="Почати",size_hint=(0.3,0.15),pos_hint={'center_x': 0.5, ' top': 0.3})
        self.btn.on_press=self.next
        
        layout.add_widget(instr)
        layout.add_widget(lbl1)
        layout.add_widget(lbl2)
        layout.add_widget(self.in_name)
        layout.add_widget(self.in_age)
        layout.add_widget(self.btn)
        self.add_widget(layout)
    def next(self):
        global name
        global age
        name = self.in_name.text
        age = self.in_age.text
        print(age)
        print(name)
        #self.manager.current="pulse1"
        
        


class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name="instr")) #1 екран
        #sm.add_widget(PulseScr(name="pulse1")) #2 екран
        #sm.add_widget(CheckSits(name="sits")) #3 екран
        #sm.add_widget(PulseScr2(name="pulse2")) #4 екран
        #sm.add_widget(Result(name="result")) #5 екран
        return sm
app = HeartCheck()
app.run()