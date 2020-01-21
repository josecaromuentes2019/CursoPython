#en python un alista puede tener difereftes tipos de datos

#declaracion de lista
numeros = [1,4,5,'Jose',7]

#para mostrar toda la lista se usa el nombre del la lista con conchetes 
#y dos puntos dentro, o el nombre de la lista sin corchetes
print('se imprime lista ',numeros)

#para agregar al final de la lista se usa append()
numeros.append(9)
print(numeros[:])

#para agregar en una posicion de la lista se usa inset() el primer parametro indica 
#el indice y el segundo el valor
numeros.insert(2,90)
print(numeros[:])

#para agregar varios datos auna lista se usa extend() y se le pasan
#los valores en su respectivo corchete
numeros.extend([78,34,12,34])
print('contatenamos con exted ',numeros[:])

#para imprimir una porcion de la lista usamos la siguiente intruccion,
#donde el primer parametro indica el primer indice (inclusibe) y el segundo 
# parametro indica el segundo indice (no inclusibe)
print(numeros[2:4])

#si solo incluimos el primer indice impre desde ese indice (inclusibe) hasta el final
print(numeros[2:])

#si solo se incluye el ultimo indice imprime desde el inicio de la lista 
#hasta dicho indice (no inclusibe)
print(numeros[:4])

#si incluye solo un indice sin puntos ningunos imprime el valor en esa posicion,
#teniendo en cuenta que inicia de cero
print(numeros[2])

#si se pasa un indice negativo imbierte el orden de impresion tomando el ultimo 
#comoprimero en este caso no inicia de cero
print(numeros[-3])

#para retornar el indice de un valor en la lista se usa index() y se pasa el valor,
#si el valor esta repetido devuelve el primero que encuentra
print(numeros.index(90))

#para buscar un elementoen la lista se usa la in esta
#funcion debuelve true si esta y false si no esta
print(34 in numeros)

#para eliminar cualquier elemento de un alista se usa remove()
numeros.remove(90)
print(numeros[:])


#para eliminar al final de la lista usamos pop() si se pasa un indice por 
#parametro elimina lo que hay en ese indice pop(3)
numeros.pop(3)
print('AQUI ELIMINAMOS ',numeros[:])

#para concatenar o unir dos listas usamos el signo mas (+)
variado =['Luna',2.4,True,8]
miLista = numeros + variado
print(miLista[:])

#para repetir el contenido de un alista usamos el sigbo multiplicacion (*)
variado1 = variado*3

print(variado1[:])

#cuantas veces esta un elemento en una lista
print('cuantas veces esta un elemento ',variado1.count('Luna'))

#para saber cuantos elementos tiene un lista
print(len(variado))