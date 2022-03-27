from logging import root
from kivy.uix.label import Label
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import ListProperty

class CustomDropdown(DropDown):
    pass

class DropdownButton(ButtonBehavior, Label):
    cor1 = ListProperty([0.1, 0.5, 0.7, 1])
    cor2 = ListProperty([0, 0.1, 0.3, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dropdown = DropDown()
        self.currencies = []
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
            Rectangle(size=self.size, pos=self.pos)
            """ Ellipse(size=(self.height,self.height), pos=self.pos)
            Ellipse(size=(self.height, self.height), 
                pos=(self.x+self.width-self.height,self.y))
            Rectangle(size=(self.width-self.height,self.height),
                pos=(self.x+self.height/2.0,self.y)) """

    def AtualizarLista(self, *args):
        for option in self.currencies:
            botao = Button(text=option['name'], size_hint_y=None, height=30, font_size=15)
            botao.bind(on_release=lambda botao: self.Selecionar(botao.text))
            self.dropdown.add_widget(botao)
        #self.dropdown.bind(on_select = lambda instance, x: self.Selecionar(x['code'], x['name']))

    def Selecionar(self, name, *args):
        self.dropdown.dismiss()
        self.text = name

    def on_release(self, *args):
        self.dropdown.open(self)


class Input(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_text(self, instance, value):
        self.text = value


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
            Rectangle(size=self.size, pos=self.pos)