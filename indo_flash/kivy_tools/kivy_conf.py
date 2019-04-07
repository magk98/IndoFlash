from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label




class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1

        self.inside = BoxLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Wybierz język", font_size=20))
        self.add_widget(self.inside)

        self.button_indo = Button(text='indo', font_size=20)
        self.button_pl = Button(text='polski', font_size=20)
        self.button_indo.bind(on_press=self.indo_pressed)
        self.button_pl.bind(on_press=self.pl_pressed)
        self.add_widget(self.button_indo)
        self.add_widget(self.button_pl)

    def indo_pressed(self, instance):
        lang = "indo"
        print(lang)

    def pl_pressed(self, instance):
        lang = "pl"
        print(lang)


class DictionaryApp(Widget, App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    DictionaryApp().run()
