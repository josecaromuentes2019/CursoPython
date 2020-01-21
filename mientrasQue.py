print('este preograma determina si un aedad es correcta')

edad = int(input('digita tu edad '))
contador = 0

while edad<0 or edad>100:
    print('has introducido una edad incorecta')
    edad =int(input('digita tu edad '))
    contador +=1
    if contador==2:
        print('Por seguridad el programa finalizara')
        break

if contador<2:
    print('la edad es correcta')
else:
    print('Lo siento agotaste los intentos')
