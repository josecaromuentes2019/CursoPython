def numerosPares(numero):
    num = 1
    while num<numero:
        yield num * 2
        num +=1

pares = numerosPares(10)

print(next(pares))
print(next(pares))
print(next(pares))

print('')
print('')

#cuando el parametro es presedido por un * significa que la funncion resibe varios parametros
def ciudades(*mis_ciudades):
    for elemento in mis_ciudades:
        yield from elemento


city = ciudades('Medellin','Barranquilla','Cali','Monteria','ibague','bogota','pasto')
print(next(city))
print(next(city))
print(next(city))


mi_lista =[3,6,7,1,5,4,2]
print(mi_lista)
mi_lista.pop(0)
print('eliminamos elemento en posicion 0 con pop(0) ',mi_lista)
print(sorted(mi_lista))
#invierte la lista
print(mi_lista[::-1])

