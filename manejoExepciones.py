def divide():
    while True:
        try:
            opc1 =float(input('digita el primer numero '))
            opc2 =float(input('digita el segundo numero '))

            print('Resultado Division: '+str(opc1/opc2))
            print('Operacion terminada')
            break
        except ValueError:
            print('digitaste un caracter debes digitar un numero')
        except ZeroDivisionError:
            print('No es posible dividir por cero')

divide()