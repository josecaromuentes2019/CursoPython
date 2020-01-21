print('Verificacion de usuario')

edad_usuario = int(input('Introduce tu edad '))

if edad_usuario < 18:
    print('No puedes pasar, eres un niño')
elif edad_usuario > 70:
    print('No puedes pasar, Eres Adulto mayor')
else:
    print('Puedes pasar, estas en edad optima')