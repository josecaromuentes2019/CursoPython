from tkinter import *


root=Tk()
root.title('Trabajo Tkinter')
root.iconbitmap('graficos/img/azul.ico')

def suma():
    try:
        resultado.set(float(numero1.get()) + float(numero2.get()))
    except:
        print('ocurrio un error')

def resta():
    try:
        resultado.set(float(numero1.get()) - float(numero2.get()))
    except ValueError :
        print('digita un numero')

numero1= StringVar()
numero2= StringVar()
resultado = StringVar()

frame = Frame(root)
frame.config(bd=25)
frame.pack()

#creacion de labels
labelnum1 = Label(frame,text='Numero 1')
labelnum1.grid(row=0,column=0)

labelnum2 = Label(frame,text='Numero 2')
labelnum2.grid(row=2,column=0)

labelres = Label(frame,text='Resultado')
labelres.grid(row=6,column=0)

#creacion de caja de texto
entrynum1= Entry(frame,justify='center', textvariable=numero1)
entrynum1.grid(row=1,column=0)

entrynum2= Entry(frame,justify='center', textvariable=numero2)
entrynum2.grid(row=4,column=0)

entryres= Entry(frame,justify='center',textvariable=resultado ,state='disable')
entryres.grid(row=7,column=0)

#creacion de botones
btnsuma = Button(frame,text='Sumar',command=suma)
btnsuma.grid(row=5,column=0,pady=10,sticky='w')

btnresta = Button(frame,text='Restar',command=resta)
btnresta.grid(row=5,column=0,pady=10,sticky='e')

root.mainloop()