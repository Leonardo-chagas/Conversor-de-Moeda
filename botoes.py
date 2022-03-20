from cv2 import ellipse
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.dropdown import DropDown
from kivy.uix.image import Image
from kivy.properties import ListProperty
import requests


class Dropdown(ButtonBehavior, Image):
    currencies = []
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open('moedas.txt') as f:
            for line in f:
                content = line.split(' ')
                currency = {'code': content[0], 'name': ' '.join(content[1:])}
                self.currencies.append(currency)


class Botao(ButtonBehavior):
    cor1 = ListProperty([0.1, 0.5, 0.7, 1])
    cor2 = ListProperty([0, 0.1, 0.3, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Atualizar()

    def on_pos(self, *args):
        self.Atualizar()
    
    def on_size(self, *args):
        self.Atualizar()
    
    def on_cor(self, *args):
        self.Atualizar()
    
    def Atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.cor1)
            Ellipse(size=self.size, pos=self.pos)