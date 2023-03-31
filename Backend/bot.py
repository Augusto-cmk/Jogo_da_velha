from random import randint
import numpy as np
from Backend.logical import GameStruct

def change(value:str):
    if value == 'o':
        return 2
    elif value == 'x':
        return 1
    else:
        return 0
    
class Bot:
    def __init__(self,itsPlayer:bool,name:str) -> None:
        self.player = itsPlayer
        self.name = name
        self.pos = {"1":(0,0),"2":(0,1),"3":(0,2),
                    "4":(1,0),"5":(1,1),"6":(1,2),
                    "7":(2,0),"8":(2,1),"9":(2,2)}
    
    def isPlayer(self)->bool:
        return self.player
    
    def getName(self):
        return self.name

    def play(self,plays:list):# Refere-se a jogada que o bot vai fazer, e para isso ele recebe a lista com os dados da partida, referente as 9 posições
        return self.__get_best_play(plays)

    def __get_best_play(self,plays:list):
        plays = np.array(plays)
        possibilidades = [i+1 for i in range(len(plays)) if plays[i] == None]# Obtendo os locais que o bot pode jogar
        for possibilidade in possibilidades:
            teste1 = plays.copy().tolist()
            teste1[possibilidade-1] = 'x'
            resultado1 = self.__get_struct(teste1).getVencedor()

            teste2 = plays.copy().tolist()
            teste2[possibilidade-1] = 'o'
            resultado2 = self.__get_struct(teste2).getVencedor()

            if resultado2 == 'o':
                return possibilidade
        

        for possibilidade in possibilidades:
            teste1 = plays.copy().tolist()
            teste1[possibilidade-1] = 'x'
            resultado1 = self.__get_struct(teste1).getVencedor()

            if resultado1 == 'x':
                return possibilidade

        if 5 in possibilidades:
            return 5
        else:
            JogadasX = [i+1 for i in range(len(plays)) if plays[i] == 'x']
            Impares = [i+1 for i in range(len(plays)) if plays[i] == 'x' and (i+1)%2 != 0]
            if len(Impares) == len(JogadasX) and len(JogadasX) > 1:
                posicoes = [i for i in possibilidades if i%2 == 0]    
            else:
                posicoes = [i for i in possibilidades if i%2 != 0]
            return posicoes[randint(0,len(posicoes)-1)]


    
    def __get_struct(self,teste:list)->GameStruct:
        struct = GameStruct()
        for i in range(len(teste)):
            indexX,indexY = self.pos[str(i+1)]
            struct.insertValue(indexX,indexY,teste[i])
        return struct
    
    def __have_two_options(self,plays:list,player:str):
        possibilidades = [i+1 for i in range(len(plays)) if plays[i] == None]# Obtendo os locais que o bot pode jogar
        win = 0
        for possibilidade in possibilidades:
            teste = plays.copy()
            teste[possibilidade-1] = player
            resultado = self.__get_struct(teste).getVencedor()
            if resultado == player:
                win += 1
        
        return win == 2


