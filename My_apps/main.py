from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from instructions import txt_instruction, txt_test1, txt_test2,txt_test3, txt_sits
from ruffier import test


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
        age = int(self.in_age.text)
        self.manager.current='pulse1'
        self.manager.transition.direction = 'up'
        
class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        instr = Label(text=txt_test1,size_hint=(0.9, 0.2), pos_hint={'center_x': 0.5, 'top': 0.9})
        lbl_result = Label(text="Введіть результат", size_hint=(0.3,0.1), pos_hint={'x':0.1, 'top': 0.45})
        self.in_result=TextInput(multiline=False,size_hint=(0.4,0.1),pos_hint={'x': 0.4, 'top': 0.5})
        self.btn=Button(text="Продовжити",size_hint=(0.3,0.15),pos_hint={'center_x': 0.5, ' top': 0.3})
        self.btn.on_press=self.next
        
        
        layout.add_widget(instr)
        layout.add_widget(lbl_result)
        layout.add_widget(self.in_result)
        layout.add_widget(self.btn)
        self.add_widget(layout)
    def next(self):
        global p1
        p1=int(self.in_result.text)
        self.manager.current="sits"
        self.manager.transition.direction = 'down'

class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        instr = Label(text=txt_sits,size_hint=(0.9, 0.2), pos_hint={'center_x': 0.5, 'top': 0.9})
  
        self.btn=Button(text="Продовжити",size_hint=(0.3,0.15),pos_hint={'center_x': 0.5, ' top': 0.3})
        self.btn.on_press=self.next   
        layout.add_widget(instr)
        layout.add_widget(self.btn)
        self.add_widget(layout)
    def next(self):
        self.manager.current="pulse2"
        self.manager.transition.direction = 'left'

class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        instr = Label(text=txt_test3,size_hint=(0.9, 0.2), pos_hint={'center_x': 0.5, 'top': 0.9})
        lbl1 = Label(text="Результат", size_hint=(0.3,0.1), pos_hint={'x':0.1, 'top': 0.45})
        lbl2 = Label(text="Результат Після Відпочинку", size_hint=(0.3,0.1), pos_hint={'x':0.1, 'top': 0.6})
        self.in_result1=TextInput(multiline=False,size_hint=(0.4,0.1),pos_hint={'x': 0.4, 'top': 0.5})
        self.in_result2=TextInput(multiline=False,size_hint=(0.4,0.1),pos_hint={'x': 0.4, 'top': 0.6})
        self.btn=Button(text="Завершити",size_hint=(0.3,0.15),pos_hint={'center_x': 0.5, ' top': 0.3})
        self.btn.on_press=self.next
        
        layout.add_widget(instr)
        layout.add_widget(lbl1)
        layout.add_widget(lbl2)
        layout.add_widget(self.in_result1)
        layout.add_widget(self.in_result2)
        layout.add_widget(self.btn)
        self.add_widget(layout)
    def next(self):
        global p2,p3
        p2=int(self.in_result1.text)
        p3=int(self.in_result2.text)
        self.manager.current="result"
        self.manager.transition.direction = 'right'

class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        self.lbl1=Label(text="",size_hint=(0.9, 0.2), pos_hint={'center_x': 0.5, 'top': 0.9})
     
        layout.add_widget(self.lbl1)

        self.add_widget(layout)
        self.on_enter=self.before
    def before(self):
        global name
        self.lbl1.text=name +'\n' + test(p1,p2,p3,age)
        self.manager.transition.direction = 'up'

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name="instr")) #1 екран
        sm.add_widget(PulseScr(name="pulse1")) #2 екран
        sm.add_widget(CheckSits(name="sits")) #3 екран
        sm.add_widget(PulseScr2(name="pulse2")) #4 екран
        sm.add_widget(Result(name="result")) #5 екран
        return sm
app = HeartCheck()
app.run()