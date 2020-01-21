from tkinter import *

raiz = Tk()
raiz.title('Primera Ventana')
raiz.config(bg='blue')
raiz.iconbitmap('graficos/img/azul.ico')
raiz.config(bd=5)
raiz.config(relief='groove')

miframe = Frame()
miframe.pack(expand=1)
miframe.config(bg='red')
miframe.config(width="400",height="250") #width=480,height=320
miframe.config(bd=5)
miframe.config(relief='ridge')

raiz.mainloop()
