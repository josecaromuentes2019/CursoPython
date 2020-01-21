import sqlite3
from tkinter import * 

root = Tk()



frame = Frame(root)
frame.pack()
frame.config(bd=14)
juguete = StringVar()
precio= StringVar()
seccion = StringVar()

def enviadatos():
    #global micursor
    miconexion = sqlite3.connect('BBDD/gestionarproductos')
    micursor = miconexion.cursor()
    if juguete.get() !='' and precio.get() != '' and seccion.get() != '':
        lt=[]
        milista=[juguete.get(),int(precio.get()),seccion.get()]
        lt.append(milista)  
        micursor.executemany('INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)',lt)

    miconexion.commit()
    miconexion.close()
    juguete.set('')
    precio.set('')
    seccion.set('')

Label(frame,text='Agregar Informacion a la base de datos',fg='red').grid(row=1,column=1,pady=5,padx=5,columnspan=2)

Label(frame,text='Juguete:').grid(row=2,column=1,sticky='w')
entryjuguete = Entry(frame,textvariable=juguete)
entryjuguete.grid(row=2,column=2)

Label(frame,text='Precio:').grid(row=3,column=1,sticky='w')
entryprecio = Entry(frame,textvariable=precio)
entryprecio.grid(row=3,column=2)

Label(frame,text='Seccion:').grid(row=4,column=1,sticky='w')
entryseccion = Entry(frame,textvariable=seccion)
entryseccion.grid(row=4,column=2)




Button(frame,text='Enviar',cursor='hand2',command=enviadatos).grid(row=5,column=2,sticky='e')

#las lineas comentadas crean la tabla y almacenan informacion son comentadas porque ya 
#fueron usadas y pueden causar error al ejecutar nuevamente el codigo

#misarticulos=[
#    ('Camion',10000,'Jugueteria'),
#    ('Zapatos',90000,'Deportes'),
#    ('Tinaja',30000,'Ceramica')
#]

#micursor.execute('''
#CREATE TABLE productos (
#ID INTEGER PRIMARY KEY AUTOINCREMENT,
#NOMBREARTICULO VARCHAR(50),
#PRECIO INTEGER,
#SECCION VARCHAR(20)
#)''')

#micursor.executemany('INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)',misarticulos)

#consultar registros
#res_sql=micursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'Jugueteria'")
#listaproductos = res_sql.fetchall()
#print(listaproductos[0][3])

#actualisar registros
#li=micursor.execute("UPDATE PRODUCTOS SET PRECIO=10000 WHERE PRECIO=12000")
#listaproductos=li.fetchall()
#print(listaproductos)


root.mainloop()