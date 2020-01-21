import math

print('este programa calcula raiz cuadrada')
numero = int(input('Digita un numero '))
intentos =0
while numero < 0:
    intentos +=1
    if(intentos == 3):
        print('el programa finalizo por exeso de intentos')
        break
    print('no es posible calcular raices negativas te restan '+str(3-intentos)+' intentos')
    numero = int(input('Digita un numero '))

if intentos<3:
    resultado = math.sqrt(numero)
    print(f'La raiz cuadrada de {numero} es {resultado}' )
else:
    print('lo sentimos intenta mas tarde')