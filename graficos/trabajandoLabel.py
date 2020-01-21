from tkinter import *

root = Tk()
root.title('Usando Label')
root.iconbitmap('graficos/img/azul.ico')
frame = Frame(root,width=400,height=250)
frame.pack()
imagen = PhotoImage(file="graficos/img/descarga.png")
label = Label(frame,image=imagen)
label.place(x=0,y=0)

#canvas = Canvas( label,width=100, height=100)
#canvas.place(x=50,y=40)
#canvas.create_text(50, 50, text="Hola mundo!")
miLabel = Label(label,text='mi texto',fg='red')
miLabel.place(x=50,y=40 )

root.mainloop()