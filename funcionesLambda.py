numpar = lambda numero: numero%2 == 0
print(numpar(2))

#funcion filter se puede aplicar tanto a listas como a objetos
lisnumeros =[2,3,5,6,7,8,9,10]
print(list(filter(lambda num: num % 2 == 0,lisnumeros)))

class Empleado:
    def __init__(self,nombre,salario):

        self.nombre = nombre
        self.salario = salario

    def __str__(self):

        return '{} tiene un salario de {}'.format(self.nombre,self.salario)

empleados = [
    Empleado('juan',2000),
    Empleado('Maria',3000),
    Empleado('Carlos',2500),
    Empleado('Estjer',3500)
]

resultado = filter(lambda empleado : empleado.salario <= 2000,empleados)

for res in resultado:
    print(res)
