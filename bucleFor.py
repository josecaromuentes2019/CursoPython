for i in ['luis', 'diana', 'esther', 'andres']:
    print('hola')
    
email = "josecar1487@gmail.com"
if email.count("@")>1 or email.count("@")==0:
    print('correo invalido')
else:
    print('correo valido')

#recorrer un bucle de dos en dos

for i in range(0,10,2):
    print(f'Dato numero {i}')


print(len(email))