from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.dropdown import DropDown
import requests


class Dropdown(ButtonBehavior):
    currencies = []
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
