from kivy.graphics import Rectangle,Color
from kivy.uix.widget import Widget

class Fundo(Widget):
    def __init__(self,tam_x,tam_y,cor,pos_x=None,pos_y=None, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(cor[0],cor[1],cor[2],cor[3])
            if pos_x == None and pos_y == None:
                self.rect = Rectangle(size=[tam_x,tam_y])
            else:
                self.rect = Rectangle(size=[tam_x, tam_y],pos=(pos_x,pos_y))