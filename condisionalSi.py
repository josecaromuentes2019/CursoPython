print('Programa de evaluacion de notas')

#input() se usa para que el programa espera un valor por teclado
miNota = input('Digita una nota ')
def evaluacion(nota):
    valoracion ='Aprobado'
    if nota<5:
        valoracion = 'Aplazado'
    
    return valoracion
#int()se usa para pasar de string a entero
print(evaluacion(int(miNota)))
