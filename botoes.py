from logging import root
from kivy.uix.label import Label
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import ListProperty

class DropdownButton(ButtonBehavior, Label):
    currencies = []
    dropdown = DropDown()
    cor1 = ListProperty([0.1, 0.5, 0.7, 1])
    cor2 = ListProperty([0, 0.1, 0.3, 1])
    codigo = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open('moedas.txt', encoding="utf8") as f:
            for line in f:
                content = line.split(' ')
                currency = {'code': content[0], 'name': ' '.join(content[1:])}
                self.currencies.append(currency)
        self.Atualizar()
        self.AtualizarLista()

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

    def AtualizarLista(self, *args):
        for option in self.currencies:
            botao = Button(text=option['name'], size_hint_y=None, size=(30, 20))
            botao.bind(on_release=lambda x: self.Selecionar(option['code'], option['name']))
            self.dropdown.add_widget(botao)

    def Selecionar(self, code, name, *args):
        self.dropdown.dismiss()
        self.text = name
        self.codigo = code
        print(name)

    def on_release(self, *args):
        self.dropdown.open(self)


class Input(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = '0,00'
    
    def on_text(self, *args):
        x = 5


class Botao(ButtonBehavior, Label):
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