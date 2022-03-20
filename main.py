from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import requests

key = '68480ca7c26cbc361957e9a6'

class Gerenciador(BoxLayout):
    pass

class Aplicativo(App):
    def build(self):
        return Gerenciador()

Aplicativo().run()