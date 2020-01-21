#las tuplas no se pueden modificar, estas se distinguen de las listas porque usan () 
#y en su interior lo svalores

#declaracio de un atupla
miTupla = (1,4,2,3,'mi Tupla')
print(miTupla)

#buscar eleneto de la tupla por indice
print('Busqueda por Indice ',miTupla.index(3))
print('numero de elentos en la tupla ',len(miTupla))

#para obtener un valor por indice en una tupla se usa [] y en su interior el indice
print(miTupla[2])

#para pasar un tupla a lista usamos el metodo list() 
#pasandle com parametrois una tupla
tuplaToLista = list(miTupla)
print("Tupla a lista ",tuplaToLista)

#para combertir de lista a tupla se usa el metodo tuple() 
#pasandole como parametros un lista
miLista = [12,'jose caro',2.45]
miTupla2 = tuple(miLista)
print('Lista a tupla ',miTupla2)

#cuantas veces esta un elemento en una Tupla
print('cuantas veces esta un valor: ',miTupla.count(1))

#saber cuantos elementos tiene un tupla
print('elementos de un atupla ',len(miTupla))

#tplas unitarias son las que llevan un solo elemento en su interior 
#este elemento debe estar seguido de un coma
tuplaUnitaria = ('Jose',)

#desempaquetado de tupla
tuplaFecha = ('Jose Caro',14,1,1987)
nombre,dia,mes,agno = tuplaFecha
print(nombre)
print(dia)
print(agno)