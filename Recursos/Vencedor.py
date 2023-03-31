from Backend.logical import GameStruct
import pandas as pd
from Backend.bot import Bot
class Winner:
    def __init__(self,playerBot=False) -> None:
        self.btns = list()
        self.struct = GameStruct()
        self.bot = Bot(playerBot,"o")
        self.pos = {"1":(0,0),"2":(0,1),"3":(0,2),
                    "4":(1,0),"5":(1,1),"6":(1,2),
                    "7":(2,0),"8":(2,1),"9":(2,2)}

    def __str__(self) -> str:
        return str(self.struct.getVencedor())
    
    def playerIsBot(self)->bool:
        return self.bot.isPlayer()
    
    def getPlaybyBot(self):
        return self.bot.play(self.struct.getPlays())

    def addBtn(self,btn):
        self.btns.append(btn)
        posX,posY = self.pos[btn.getNeme()]
        self.struct.insertValue(posX,posY,btn.getPlayer())

