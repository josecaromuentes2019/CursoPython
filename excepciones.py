while True:
    try:
        num1 =int(input('Digita el primer numero '))
        num2 =int(input('Digita el segundo numero '))
        break
    except ValueError:
        print('El valor introducido no es un numero')

oper= input('Digita una operacion: suma, resta, divide, multiplica ').lower()
print(oper)
def realizaOperacion(operacion):
    
    if operacion == 'suma':
        return num1 + num2
    elif operacion == 'resta':
        return num1 - num2
    elif operacion == 'divide':
        try:
            print(num1 / num2)
            
        except ZeroDivisionError: 
            return 'no es posible dividir por cero'
        
    elif operacion == 'multiplica':
        return num1 * num2
    else:
        print('no esta contemplada la operacion')

print(realizaOperacion(oper))

