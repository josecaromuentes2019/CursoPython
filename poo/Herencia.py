class Vehiculo():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.acelera = False
        self.enMarcha = False
        self.frena = False

    def setAcelera(self):
        self.acelera = True
    
    def setEnMarcha(self):
        self.enMarcha = True
    
    def setFrena(self):
        self.frena = True
    
    def estado(self):
        print('Marca: ', self.marca, '\nModelo: ',self.modelo,
        '\nAcelera: ',self.acelera, '\nEn Marcha: ',self.enMarcha, '\nFrena: ',self.frena)


class Moto(Vehiculo):
    hPicar = ''

    def picar(self):
        self.hPicar ='Voy picando'

    def estado(self):
        super().estado()
        self.picar()
        print(self.hPicar)

objMoto = Moto('honda',2019)
objMoto.estado()           