from tkinter import *
root = Tk()

frame = Frame(root)
frame.pack()
Label(frame,text='Lugares de viaje').pack()
turismo=IntVar()
ciudad=IntVar()
rural=IntVar()

def destino():
    tomavalor=''
    if turismo.get() == 1:
        tomavalor +=' Turismo'
        print(tomavalor)

    if ciudad.get() == 1:
        tomavalor +=' Ciudad'
        print(tomavalor)

    if rural.get() == 1:
        tomavalor +=' Rural'
        print(tomavalor)

    milabel.config(text=tomavalor)
    


Checkbutton(frame,text='Turismo',variable=turismo,onvalue=1,offvalue=0,command=destino).pack()
Checkbutton(frame,text='Ciudad',variable=ciudad,onvalue=1,offvalue=0,command=destino).pack()
Checkbutton(frame,text='Rural',variable=rural,onvalue=1,offvalue=0,command=destino).pack()

milabel=Label(frame)
milabel.pack()

root.mainloop()