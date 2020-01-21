class Mi_Coche():

    def __init__(self):
        self.__largo  = 240
        self.__alto = 180
        self.__num_llantas = 4
        self.__estado = False



    
    def enMarcha(self,arranca):
        self.__estado = arranca
        if self.__estado:
            boolVerifica = self.__verifica()

        
        if self.__estado and boolVerifica:
            print('El auto esta en movimiento')
        elif self.__estado and boolVerifica == False:
            print('algo anda mal')
        else:
            print('El auto esta parqueado')
    
    def __verifica(self):
        puertas = 'ok'
        gasolina= 'no'

        if puertas == 'ok' and gasolina == 'ok':
            return True
        else:
            return False

obj = Mi_Coche()
obj.enMarcha(True)
