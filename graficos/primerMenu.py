from tkinter import *

root= Tk()
root.title('Menu')

menuprincipal=Menu()
root.config(menu=menuprincipal)

menuarchivo=Menu(menuprincipal,tearoff=0)
menuarchivo.add_command(label='Nuevo')
menuarchivo.add_command(label='Abrir')
menuarchivo.add_command(label='Guardar')
menuarchivo.add_command(label='Cerrar')
menuarchivo.add_separator()
menuarchivo.add_command(label='Salir',command=root.quit)

menuayuda=Menu(menuprincipal,tearoff=0)
menueditar=Menu(menuprincipal,tearoff=0)

menuprincipal.add_cascade(label='Archivo',menu=menuarchivo)
menuprincipal.add_cascade(label='Editar',menu=menueditar)
menuprincipal.add_cascade(label='Ayuda',menu=menuayuda)





root.mainloop()