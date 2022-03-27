from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from botoes import *
import requests

key = '68480ca7c26cbc361957e9a6'

class Gerenciador(BoxLayout):
    def press(self):
        texto1 = self.ids.moedade.text.split('(')
        texto2 = self.ids.moedapara.text.split('(')
        erro = False
        if len(texto1) < 2:
            self.ids.errode.text = 'Você deve selecionar uma moeda!'
            erro = True
            self.ids.errode.color = (0.8, 0.1, 0.1, 1)
        else:
            self.ids.errode.text = ''
        if len(texto2) < 2:
            self.ids.erropara.text = 'Você deve selecionar uma moeda!'
            erro = True
            self.ids.erropara.color = (0.8, 0.1, 0.1, 1)
        else:
            self.ids.erropara.text = ''
        if not erro:
            if self.ids.valor.text != '':
                passou = True
                try:
                    float(self.ids.valor.text)
                except ValueError:
                    passou = False
                if passou:
                    moeda = texto1[1].strip(')\n')
                    moedaPara = texto2[1].strip(')\n')
                    valor = float(self.ids.valor.text)
                    req = requests.get('https://v6.exchangerate-api.com/v6/'+key+'/latest/'+moeda)
                    print(req.json()['conversion_rates']['PLN'])
                    valorConvertido = valor*req.json()['conversion_rates'][moedaPara]
                    self.ids.resultado.text = str(valorConvertido) + ' ' + moedaPara
                    self.ids.resultado.color = (0.9, 0.9, 0.9, 1)
                else:
                    self.ids.resultado.text = 'Você deve digitar uma valor válido!'
                    self.ids.resultado.color = (0.8, 0.1, 0.1, 1)
            else:
                self.ids.resultado.text = 'nenhum valor foi digitado'
                self.ids.resultado.color = (0.8, 0.1, 0.1, 1)

    def IsFloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

class Aplicativo(App):
    def build(self):
        #kv = Builder.load_file('aplicativo.kv')
        return Gerenciador()

Aplicativo().run()