from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from Recursos.Botao import ButtonMark
from Recursos.Vencedor import Winner
from kivy.uix.button import Button
from Recursos.fundo import Fundo
from kivy.uix.image import Image

class TelaJogo(Screen):
    def __init__(self,placar,playerBot,**kw):
        super().__init__(**kw)
        self.player = ["x"]
        self.placar = placar
        self.rl = RelativeLayout()
        self.win = Winner(playerBot)
        self.botao1 = ButtonMark(type=self.player,pos_hint={'center_x': .15, 'center_y': .87},vencedor=self.win,name="1",rl=self.rl,actionVoltar=self.voltar,placar=placar,actionBot=self.playBot,sairAction=self.sair)
        self.botao2 = ButtonMark(type=self.player,pos_hint={'center_x': .51, 'center_y': .87},vencedor=self.win,name="2",rl=self.rl,actionVoltar=self.voltar,placar=placar,actionBot=self.playBot,sairAction=self.sair)
        self.botao3 = ButtonMark(type=self.player,pos_hint={'center_x': .87, 'center_y': .87},vencedor=self.win,name="3",rl=self.rl,actionVoltar=self.voltar,placar=placar,actionBot=self.playBot,sairAction=self.sair)
        self.botao4 = ButtonMark(type=self.player,pos_hint={'center_x': .15, 'center_y': .51},vencedor=self.win,name="4",rl=self.rl,actionVoltar=self.voltar,placar=placar,actionBot=self.playBot,sairAction=self.sair)
        self.botao5 = ButtonMark(type=self.player,pos_hint={'center_x': .51, 'center_y': .51},vencedor=self.win,name="5",rl=self.rl,actionVoltar=self.voltar,placar=placar,actionBot=self.playBot,sairAction=self.sair)
        self.botao6 = ButtonMark(type=self.player,pos_hint={'center_x': .87, 'center_y': .51},vencedor=self.win,name="6",rl=self.rl,actionVoltar=self.voltar,placar=placar,actionBot=self.playBot,sairAction=self.sair)
        self.botao7 = ButtonMark(type=self.player,pos_hint={'center_x': .15, 'center_y': .15},vencedor=self.win,name="7",rl=self.rl,actionVoltar=self.voltar,placar=placar,actionBot=self.playBot,sairAction=self.sair)
        self.botao8 = ButtonMark(type=self.player,pos_hint={'center_x': .51, 'center_y': .15},vencedor=self.win,name="8",rl=self.rl,actionVoltar=self.voltar,placar=placar,actionBot=self.playBot,sairAction=self.sair)
        self.botao9 = ButtonMark(type=self.player,pos_hint={'center_x': .87, 'center_y': .15},vencedor=self.win,name="9",rl=self.rl,actionVoltar=self.voltar,placar=placar,actionBot=self.playBot,sairAction=self.sair)
        self.buttons = [self.botao1,self.botao2,self.botao3,self.botao4,self.botao5,self.botao6,self.botao7,self.botao8,self.botao9,]
        self.rl.add_widget(self.botao1)
        self.rl.add_widget(self.botao2)
        self.rl.add_widget(self.botao3)
        self.rl.add_widget(self.botao4)
        self.rl.add_widget(self.botao5)
        self.rl.add_widget(self.botao6)
        self.rl.add_widget(self.botao7)
        self.rl.add_widget(self.botao8)
        self.rl.add_widget(self.botao9)
        self.add_widget(self.rl)
    
    def playBot(self,nomeButton:str):
        self.buttons[int(nomeButton)-1].setActionBot()

    def voltar(self,obj):
        self.rl.clear_widgets()
        self.rl.add_widget(TelaJogo(self.placar,self.win.playerIsBot()))
    
    def sair(self,obj):
        self.rl.clear_widgets()
        self.add_widget(TelaInicio())


class TelaInicio(Screen):
    def __init__(self,**kw):
        super().__init__(**kw)
        self.rl = RelativeLayout()
        self.placar = {"Player 1":0,"Player 2":0}
        imagem = Image(source='Imagens/Fundo_Inicial.jpg',pos_hint={'center_x': .5, 'center_y': .5})
        fundo = Fundo(2000,1000,[0,0.71,1,1])
        PvP = Button(size_hint=(.09, .05),
                        pos_hint={'center_x': .45, 'center_y': .3},
                        text="PvP", on_press=self.PvP)
        
        PvB = Button(size_hint=(.09, .05),
                        pos_hint={'center_x': .55, 'center_y': .3},
                        text="PvB", on_press=self.PvB)
        self.rl.add_widget(fundo)
        self.rl.add_widget(imagem)
        self.rl.add_widget(PvP)
        self.rl.add_widget(PvB)
        self.add_widget(self.rl)
    
    
    def PvP(self,obj):
        self.rl.clear_widgets()
        self.add_widget(TelaJogo(self.placar,False))

    def PvB(self,obj):
        self.rl.clear_widgets()
        self.add_widget(TelaJogo(self.placar,True))