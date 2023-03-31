from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from Recursos.fundo import Fundo
from kivy.uix.label import Label
from kivy.uix.button import Button

class TelaVencedor(Screen):
    def __init__(self,Mensagem:str,voltarAction,placar:dict,sairAction,**kw):
        super().__init__(**kw)
        self.rl = RelativeLayout()

        telaFundo = Fundo(2000,1000,[1,1,1,1])

        labelVencedor = Label(color='black',pos_hint={'center_x': .5, 'center_y': .5}, text=Mensagem,font_size=100)

        labelPlacar = Label(color='black',pos_hint={'center_x': .5, 'center_y': .97}, text=f"Player 1 = {placar['Player 1']}  Player 2 = {placar['Player 2']}",font_size=30)

        voltar = Button(size_hint=(.1, .05),
                        pos_hint={'center_x': .05, 'center_y': .97},
                        text="Voltar", on_press=voltarAction)
        
        sair = Button(size_hint=(.1, .05),
                        pos_hint={'center_x': .15, 'center_y': .97},
                        text="Sair", on_press=sairAction)
    
        self.rl.add_widget(telaFundo)
        self.rl.add_widget(sair)
        self.rl.add_widget(labelPlacar)
        self.rl.add_widget(voltar)
        self.rl.add_widget(labelVencedor)

        self.add_widget(self.rl)


