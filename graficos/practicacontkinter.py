from tkinter import *
from io  import *
import pickle 

root = Tk()
root.title('Practica')
root.config(pady=20)
frame = Frame(root)
frame.config(padx=20,pady=20)
frame.pack()


archivoname = StringVar()
def abrearchivo():
   
    try:
        miarchivo = open(archivoname.get(),'ab+')
        miarchivo.seek(0)
        
        textarchivo.insert(END,pickle.load(miarchivo))
        
        miarchivo.close()
        del(miarchivo)

    except:
        print('ocurrio un error')


def creararchivo():
    try:
        archivonuevo = open(archivoname.get(),'wb')
        pickle.dump(textarchivo.get("0.0",END),archivonuevo)

        archivonuevo.close()
        del(archivonuevo)
        textarchivo.delete('0.0',END)
        archivoname.set('')
    except:
        print('ocurrio un error')

nombrearchivo = Label(frame,text='Nombre Archivo ',fg='blue')
nombrearchivo.grid(row=0,column=0,sticky='w')

archivolabel = Label(frame,text='Contenido Archivo ',fg='blue')
archivolabel.grid(row=1,column=0,sticky='w',pady=10)



entriachivo= Entry(frame, textvariable=archivoname)
entriachivo.grid(row=0,column=1)


textarchivo= Text(frame,width=15,height=10)
textarchivo.grid(row=1,column=1,pady=10)

scroll = Scrollbar(frame,command=textarchivo.yview)
scroll.grid(row=1,column=2,sticky='ns')
textarchivo.config(yscrollcommand=scroll.set)




btnabrir= Button(frame,text='Abrir Archivo',command=abrearchivo)
btnabrir.grid(row=2,column=0,pady=10)

btncrear= Button(frame,text='Guardar Archivo',command=creararchivo)
btncrear.grid(row=2,column=1,pady=10)



root-mainloop()