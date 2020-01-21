def primos():
    contador = 1
    num=1
    determinaPrimo = 0
    while True:
        while contador<=num:
            
            if num % contador == 0:
                determinaPrimo += 1
                if determinaPrimo > 2:
                    break
            contador +=1

        
        if determinaPrimo == 2:
            yield num
        
        determinaPrimo = 0
        num +=1
        contador = 1

numeroprimo = primos()

print(next(numeroprimo))
print(next(numeroprimo))
print(next(numeroprimo))
print(next(numeroprimo))
print(next(numeroprimo))

