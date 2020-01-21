from tkinter import *
root = Tk()
root.title('Radio')

frame = Frame(root,bd=30)
frame.pack()

label = Label(frame,text='Examen de Admision')
label.grid(row=0,column=0,pady=12)

def miresultado():
    
    contres =0
    for i,e in enumerate(listaResultados):
        if e==listacorrecta[i]:
            contres+=1
    resultado.config(text='{}'.format(round(contres*1.666)))
    mibtn.config(state='disabled')

def pregunta1():
    try:
        listaResultados.pop(0)
    except:
        print(listaResultados)
    
    listaResultados.insert(0,opcio1.get())

def pregunta2():
    try:
        listaResultados.pop(1)
    except:
        print(listaResultados)
    
    listaResultados.insert(1,opcio2.get())

def pregunta3():
    try:
        listaResultados.pop(2)
    except:
        print(listaResultados)
    
    listaResultados.insert(2,opcio3.get())


   
    
listaResultados = []
listacorrecta = [3,2,1]        


opcio1 = IntVar()
Label(frame,text='1. Los niveles de enasulamiento son:').grid(row=1,column=0,pady=20,sticky='w')
Radiobutton(frame,text='Public y Private',variable=opcio1,value=1,command= pregunta1).grid(row=2,column=0,sticky='w')
Radiobutton(frame,text='final y static',variable=opcio1,value=2,command=pregunta1).grid(row=3,column=0,sticky='w')
Radiobutton(frame,text='Public, Private, Default y Protected',variable=opcio1,value=3,command=pregunta1).grid(row=4,column=0,sticky='w')

opcio2 = IntVar()
Label(frame,text='2. Que es un Objeto:').grid(row=5,column=0,pady=20,sticky='w')
Radiobutton(frame,text='modelo para crear una clase',variable=opcio2,value=1,command=pregunta2).grid(row=6,column=0,sticky='w')
Radiobutton(frame,text='Intancia de una clase',variable=opcio2,value=2,command=pregunta2).grid(row=7,column=0,sticky='w')
Radiobutton(frame,text='Ninguna',variable=opcio2,value=3,command=pregunta2).grid(row=8,column=0,sticky='w')


opcio3 = IntVar()
Label(frame,text='3. Que es la sobrecarga').grid(row=9,column=0,pady=20,sticky='w')
Radiobutton(frame,text='metodo con mismo nombre y parmetros diferentes',variable=opcio3,value=1,command=pregunta3).grid(row=10,column=0,sticky='w')
Radiobutton(frame,text='clase con metodo protected',variable=opcio3,value=2,command=pregunta3).grid(row=11,column=0,sticky='w')
Radiobutton(frame,text='todas la anteriores',variable=opcio3,value=3,command=pregunta3).grid(row=12,column=0,sticky='w')


Label(frame,text='Resultado:').grid(row=14,column=0)
resultado=Label(frame)
resultado.grid(row=15,column=0)
mibtn=Button(frame,text='Enviar',command=miresultado,cursor='hand2')
mibtn.grid(row=16,column=0)

root.mainloop()