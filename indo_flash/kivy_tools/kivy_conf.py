from kivy.app import App
from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty
from Dictionary import Dictionary
#todo trzeba jakos ogarnac zeby glowny label zmienial slowka, bo obecnie dziala check_all, trzeba zmodyfikowac check_all

class LoginScreen(ButtonBehavior, FloatLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        l = Label(
            text='[size=24][i]Wybierz język[/i][/size]',
            markup=True,
            pos_hint={'center_x': 0.5, 'center_y': 0.8})
        b1 = Button(
            text='PL',
            pos_hint={'center_x': 0.25, 'center_y': 0.2},
            size_hint=(0.5,0.5),
            font_size=24
        )
        b2 = Button(
            text='INDO',
            pos_hint={'center_x': 0.75, 'center_y': 0.2},
            font_size=24,
            size_hint=(0.5,0.5)
        )
        self.add_widget(l)
        self.add_widget(b1)
        self.add_widget(b2)

    def on_press(self):
        self.remove_widget(self.l)
        nowy = Label(text='nic')
        self.add_widget(nowy)


class DictionaryApp(App):
    def build(self):
        return LoginScreen()



if __name__ == '__main__':
    DictionaryApp().run()
