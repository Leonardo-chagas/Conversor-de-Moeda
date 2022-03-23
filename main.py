from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from botoes import *
import requests

key = '68480ca7c26cbc361957e9a6'

class Gerenciador(BoxLayout):
    pass

class Aplicativo(App):
    def build(self):
        #kv = Builder.load_file('aplicativo.kv')
        return Gerenciador()

Aplicativo().run()