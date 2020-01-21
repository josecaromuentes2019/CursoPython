import math

class Punto():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def cuadrante(self):
        if self.x > 0 and self.y >0:
            print(f'{self} Pertenece al primer Cuadrante')
        
        elif self.x < 0 and self.y > 0:
            print(f'{self} Pertenece al segundo Cuadrante')

        elif self.x <0 and self.y <0:
            print(f'{self} Pertenece al tercer Cuadrante')
        
        elif self.x > 0 and self.y <0:
            print(f'{self} Pertenece al cuarto Cuadrante')
        
        else:
            print(f'{self} Estamos en el Origen')

    def vector(self,p):
        print(f'El vector resultante entre {self} y {p} es: ({p.x-self.x},{p.y-self.y})')

    def distancia(self,p):

        inx = (p.x-self.x)**2
        iny = (p.y-self.y)**2

        print(f'La distancia en tre los puntos {p} y {self} es: {round(math.sqrt(inx+iny),2)}')
        




A = Punto(3,2)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto()

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)
