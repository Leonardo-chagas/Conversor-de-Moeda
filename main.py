from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import requests

class Gerenciador(BoxLayout):
    pass

class Aplicativo(App):
    def build(self):
        return Gerenciador()

Aplicativo().run()