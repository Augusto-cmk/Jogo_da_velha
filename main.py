from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from Telas.jogo import TelaInicio
import pandas as pd

class GerenciadorTelas(ScreenManager):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.add_widget(TelaInicio())


class Jogo_da_Velha(App):
    def build(self):
        return GerenciadorTelas()

Jogo_da_Velha().run()