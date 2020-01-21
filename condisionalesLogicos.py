print('Este programa determina si tienes derecho a veca')

distancia_vivienda = int(input('A cuantos km vives de la escuela '))
num_hermanos = int(input('Cuantos hermanos tienes en medio '))
ingresos = float(input('Cuantos son los ingresos  anuales familiares '))

if distancia_vivienda>40 and num_hermanos>=3 or ingresos<20000 :
    print('Tienes derecho a beca')
else:
    print('NO tienes derecho a beca')

print('Elige una asignatura optativa')
print('Desarrollo de software, Configuracion de redes, Analisis de sistenas')
asignatura = input('Digita una asignatura ').lower()
listaAsignaturas = ('desarrollo de software','configuracion de redes','analisis de sistenas')
print(asignatura)
if asignatura in listaAsignaturas:
    print('Acabas de quedar inscrito')
else:
    print('Digita una asignatura Valida')