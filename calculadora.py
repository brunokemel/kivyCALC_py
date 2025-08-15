from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operatos = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None