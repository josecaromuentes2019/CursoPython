import math

print('estre programa calcula la Raiz cuadrada de un numero')

def raiz(num):
    if num<0:
        raise ValueError('No es posible calcular Raices negativas')
    else:
        return math.sqrt(num)

while True:
    try:
        numero = int(input('Digita un numero: '))
        print(raiz(numero))
    except ValueError as miError:
        print(miError)
    else:
        print('Progrma finalizado')
        break