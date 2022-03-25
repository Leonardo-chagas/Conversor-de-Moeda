from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from botoes import *
import requests

key = '68480ca7c26cbc361957e9a6'

class Gerenciador(BoxLayout):
    def press(self):
        if self.ids.valor.text != '':
            texto1 = self.ids.moedade.text.split('(')
            texto2 = self.ids.moedapara.text.split('(')
            moeda = texto1[1].strip(')\n')
            moedaPara = texto2[1].strip(')\n')
            valor = float(self.ids.valor.text)
            req = requests.get('https://v6.exchangerate-api.com/v6/'+key+'/latest/'+moeda)
            print(req.json()['conversion_rates']['PLN'])
            valorConvertido = valor*req.json()['conversion_rates'][moedaPara]
            self.ids.resultado.text = str(valorConvertido) + ' ' + moedaPara
        else:
            self.ids.resultado.text = 'nenhum valor foi digitado'

class Aplicativo(App):
    def build(self):
        #kv = Builder.load_file('aplicativo.kv')
        return Gerenciador()

Aplicativo().run()