exc=''
num = 5
while True:
    try:
        denominador = float(input('Digita un numero '))
        division = num/denominador
        print('Resultado de la Division: ',division)
    except Exception as e:
        if type(e).__name__ == 'ValueError':
            print('debes ingresar un numero')
        elif type(e).__name__ == 'ZeroDivisionError':
            print('no se puede dividir por cero')
    else:
        break    