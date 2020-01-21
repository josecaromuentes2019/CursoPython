import pickle

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

obj1 = Vehiculo('Mazda',2019)
obj2 = Vehiculo('Hiunday',2018)
obj3 = Vehiculo('Renault',2020)

misVehiculos = [obj1,obj2,obj3]

objbinario = open('VehiculoBinario','wb')
pickle.dump(misVehiculos,objbinario)

objbinario.close()

