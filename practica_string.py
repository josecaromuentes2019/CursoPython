email = input('Digita un correo: ')
s ='yo'

print(email.index('@'))

if email.count('@') == 1 and email.index('@') != 0 and email[-1] != '@':
    print('correcto')
else:
    print('incorrecto')
