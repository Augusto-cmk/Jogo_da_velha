from kivy.uix.button import Button
from Recursos.Vencedor import Winner
from kivy.uix.relativelayout import RelativeLayout
from Telas.Vencedor import TelaVencedor

class ButtonMark(Button):
    def __init__(self,type:list,vencedor:Winner,name:str,rl:RelativeLayout,actionVoltar,placar,actionBot,sairAction,**kw):
        super().__init__(**kw)
        self.pressed = False
        self.background_normal = "Imagens/QuadradoBranco.png"
        self.border = (0,0,0,0)
        self.imgChange = None
        self.size_hint=(.34, .34)
        self.type = type
        self.jogador = None
        self.vencedor = vencedor
        self.name = name
        self.rl = rl
        self.actionVoltar = actionVoltar
        self.sairAction = sairAction
        self.on_press = self.__action
        self.placar = placar
        self.actionBot = actionBot
    
    def setActionBot(self):
        self.jogador = self.type[0]
        self.imgChange = "Imagens/Bolinha.png"
        self.type[0] = "x"
        self.vencedor.addBtn(self)
        self.background_normal = self.imgChange
        self.pressed = True
        self.type[0] = "x"
        if str(self.vencedor) != 'None':
            jogadores = {"o":"Player 2","x":"Player 1","Velha":"Velha"}
            ganhador = jogadores[str(self.vencedor)]
            if ganhador != "Velha":
                self.rl.clear_widgets()
                self.placar[ganhador] += 1
                self.rl.add_widget(TelaVencedor(f"O {ganhador} venceu",self.actionVoltar,self.placar,self.sairAction))
            else:
                self.rl.clear_widgets()
                self.rl.add_widget(TelaVencedor(f"Velha",self.actionVoltar,self.placar,self.sairAction))

    def __action(self):
        self.__setPlayer()
        if self.pressed == False and self.imgChange:
            self.vencedor.addBtn(self)
            self.background_normal = self.imgChange
            self.pressed = True
            if str(self.vencedor) != 'None':
                jogadores = {"o":"Player 2","x":"Player 1","Velha":"Velha"}
                ganhador = jogadores[str(self.vencedor)]
                if ganhador != "Velha":
                    self.rl.clear_widgets()
                    self.placar[ganhador] += 1
                    self.rl.add_widget(TelaVencedor(f"O {ganhador} venceu",self.actionVoltar,self.placar,self.sairAction))
                else:
                    self.rl.clear_widgets()
                    self.rl.add_widget(TelaVencedor(f"Velha",self.actionVoltar,self.placar,self.sairAction))
                
                return
            if self.vencedor.playerIsBot():
                self.actionBot(self.vencedor.getPlaybyBot())

    def __setPlayer(self):
        if self.type[0] == "x" and self.pressed == False:
            self.jogador = self.type[0]
            self.imgChange = "Imagens/X.png"
            self.type[0] = "o"

        elif self.type[0] == "o" and self.pressed == False:
            self.jogador = self.type[0]
            self.imgChange = "Imagens/Bolinha.png"
            self.type[0] = "x"
    
    def getPlayer(self):
        return self.jogador

    def getNeme(self):
        return self.name
