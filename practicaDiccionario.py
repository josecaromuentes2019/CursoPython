#declaracionde diccionario usa llaves {} y es similar a un objeto json
miDiccionario = {'España':'Madrid','Argentina':'Buenos Aires','Colombia':'Bogota','Peru':'Lima'}

#imprimir todo un diccionario
print(miDiccionario)

#imprimir una valor de una clave en un diccionario
print(miDiccionario['Colombia'])

#agregar un clave mas aun diccionario existente
miDiccionario['Italia']='Lisboa'
print(miDiccionario)

#para editar se escibe igual que ara agregar pero usando la clave a editar, 
#esto sobreescribira el valor exixtente para esa clave
miDiccionario['Italia']='Roma'
print(miDiccionario)

#para eliminar una clave con su valor usamos del
del miDiccionario['Argentina']
print(miDiccionario)

#diccionario con Tuplas, tambien admite listas
otroDicc = {21:'Jordan','nombre':'Michael','Chuipo':'Chicago','anillos':[1991,1992,1996,1997,1998]}
print(otroDicc)
otroDicc['anillos'].append(2020)
print(otroDicc)

#longitud del diccionario
print('Longitud del diccionario ',len(otroDicc))

#mostrar las claves
print(otroDicc.keys())

#mostrar valores
print(otroDicc.values())

#elimina un aclave con su valor, paando como parametro un aclave
otroDicc.pop('anillos')
print('aqui se elimina por clave ',otroDicc)