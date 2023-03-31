class GameStruct:
    def __init__(self):
        self.matrix = self.__contructMatrix()
        self.sizeX = 3
        self.sizeY = 3
        self.vencedor = None

    def __contructMatrix(self):
        return [[None for i in range (3)] for j in range(3)]
    
    def __notHaveNone(self):
        for lista in self.matrix:
            if None in lista:
                return False
        
        return True


    def insertValue(self,posx:int,posy:int,Value:str):
        self.matrix[posx][posy] = Value
    
    def getPlays(self)->list:
        plays = []
        for i in range(3):
            for j in range(3):
                plays.append(self.matrix[i][j])
        return plays

    def getValue(self,posx:int,posy:int):
        return self.matrix[posx][posy]

    def getVencedor(self):
        diagPrincipal,diagSecundaria,(vencedorPrincipal,vencedorSecundaria) = self.__diagonais()
        
        hor1,hor2,hor3,(vencH1,vencH2,vencH3) = self.__horizontais()

        vert1,vert2,vert3,(vencV1,vencV2,vencV3) = self.__verticais()


        if diagPrincipal and vencedorPrincipal != None:
            self.vencedor = vencedorPrincipal
        elif diagSecundaria and vencedorSecundaria != None:
            self.vencedor = vencedorSecundaria
        elif hor1 and vencH1 != None:
            self.vencedor = vencH1
        elif hor2 and vencH2 != None:
            self.vencedor = vencH2
        elif hor3 and vencH3 != None:
            self.vencedor = vencH3
        elif vert1 and vencV1 != None:
            self.vencedor = vencV1 
        elif vert2 and vencV2 != None:
            self.vencedor = vencV2 
        elif vert3 and vencV3 != None:
            self.vencedor = vencV3
        elif self.__notHaveNone():
            return "Velha"

        return self.vencedor

    def __diagonais(self): # Verifica as diagonais
        pos1 = self.matrix[0][0]
        pos2 = self.matrix[1][1]
        pos3 = self.matrix[2][2]

        pos4 = self.matrix[0][2]
        pos5 = self.matrix[1][1]
        pos6 = self.matrix[2][0]

        return pos1 == pos2 == pos3,pos4 == pos5 == pos6,(pos1,pos4)
    
    def __horizontais(self): # Verifica as horizontais
        pos1 = self.matrix[0][0]
        pos2 = self.matrix[0][1]
        pos3 = self.matrix[0][2]

        pos4 = self.matrix[1][0]
        pos5 = self.matrix[1][1]
        pos6 = self.matrix[1][2]

        pos7 = self.matrix[2][0]
        pos8 = self.matrix[2][1]
        pos9 = self.matrix[2][2]

        return pos1 == pos2 == pos3,pos4 == pos5 == pos6,pos7 == pos8 == pos9,(pos1,pos4,pos7)
    

    def __verticais(self): # Verifica as horizontais
        pos1 = self.matrix[0][0]
        pos2 = self.matrix[1][0]
        pos3 = self.matrix[2][0]

        pos4 = self.matrix[0][1]
        pos5 = self.matrix[1][1]
        pos6 = self.matrix[2][1]

        pos7 = self.matrix[0][2]
        pos8 = self.matrix[1][2]
        pos9 = self.matrix[2][2]

        return pos1 == pos2 == pos3,pos4 == pos5 == pos6,pos7 == pos8 == pos9,(pos1,pos4,pos7)