salario_presidente = int(input('Digita el salario del presidente '))
print('El slario del presidente es ',salario_presidente)

salario_director = int(input('Digita el salario del director '))
print('El slario del director es ',salario_director)

salario_jefe_area = int(input('Digita el salario del jefe de area '))
print('El slario dedl jefe de area es ',salario_jefe_area)

salario_administrativo = int(input('Digita del salario del administrativo '))
print('El slario del administrativo es ',salario_administrativo)

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print('todo funciona correctamente')
else:
    print('algo anda mal')