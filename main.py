from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from botoes import *
import requests

key = '68480ca7c26cbc361957e9a6'

class Gerenciador(BoxLayout):
    def press(self):
        req = requests.get('https://v6.exchangerate-api.com/v6/'+key+'/latest/'+self.ids.moedade.codigo)
        print(req.text)

class Aplicativo(App):
    def build(self):
        #kv = Builder.load_file('aplicativo.kv')
        return Gerenciador()

Aplicativo().run()