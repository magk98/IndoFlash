from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

with open("Dictionary1.kv", encoding='utf8') as f:
    Builder.load_string(f.read())

class LoginScreen(Widget):
    b_indo = ObjectProperty(None)
    b_pl = ObjectProperty(None)

    def indo_pressed(self):
        lang = "indo"
        print(lang)

    def pl_pressed(self):
        lang = "pl"
        print(lang)


class DictionaryApp(App):
    def build(self):
        return LoginScreen()


if __name__ == "__main__":
    DictionaryApp().run()
