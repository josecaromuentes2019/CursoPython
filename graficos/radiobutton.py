from tkinter import *

root=Tk()

def sexo():
    if valor.get() == 1 :
        label.config(text='Buenos dias Señor')
        print('Buenos dias Señor')
    else:
        print('Bienos dias Señorita')
        label.config(text='Bienos dias Señorita')

valor = IntVar()

frame =Frame(root)
frame.pack()
label=Label(frame)
label.pack()
radio = Radiobutton(frame,text = 'Masculino',variable=valor,value=1,command=sexo)
radio.pack()
radio1 = Radiobutton(frame,text='Femenino',variable=valor,value=2,command=sexo)
radio1.pack()




root.mainloop()