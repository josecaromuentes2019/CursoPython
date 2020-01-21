import pickle

class Personas():

    def __init__(self,nombre,genero,edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        
        print('Se ha creado un apersona llamada ',self.nombre)
    
    def __str__(self):
        return '{} {} {} Años'.format(self.nombre,self.genero,self.edad)
    

class  ListaPersona():

    misPersonas = []
    def __init__(self):

        lpersona = open('listadepersonas.pickl','ab+')
        
        lpersona.seek(0)
        try:
            self.misPersonas = pickle.load(lpersona)  
            print('se cargaron {} personas'.format(len(self.misPersonas)))       
        except :
            print('El Archivo esta vacio')
        finally:
            lpersona.close()
            del (lpersona)

    def agrgarPersona(self,p):
        self.misPersonas.append(p)
        self.agregarPermanente()
    def mostrarPersona(self):

        for p in self.misPersonas:
            print(p)

    def agregarPermanente(self):
        abrelista = open('listadepersonas.pickl','wb')
        pickle.dump(self.misPersonas,abrelista)
        abrelista.close()
        del(abrelista)

listaP= ListaPersona()
p1 = Personas('jose','M',32)
listaP.agrgarPersona(p1)

print()
listaP= ListaPersona()
p2 = Personas('jairo','M',32)
listaP.agrgarPersona(p2)

print()
listaP= ListaPersona()
p3 = Personas('juan','M',32)
listaP.agrgarPersona(p3)
print()
listaP.mostrarPersona()
