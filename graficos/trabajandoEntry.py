from tkinter import *

#se crea ventana
root = Tk()
#se asigna titulo a ventana
root.title('trabanando con cuadros de dialogo')
# se cambia icono  de ventana
root.iconbitmap('graficos/img/azul.ico')
#se crea frame se asigna a la raiz y se le da longitud
frame_principal = Frame(root,width=500,height=350)
#se empaqueta el Frame en la raiz
frame_principal.pack()

#se crean los componentes o widgets
#creacion de los labels para identificar cuadros de texto
label_nombre = Label(frame_principal,text='Nombre : ')
#se agrega el label con un grid o regilla
label_nombre.grid(row=0,column=0,sticky = 'w',padx=10, pady=10)

#se repite lo mismo con los temas label
label_apellido = Label(frame_principal,text='Apellido : ')
label_apellido.grid(row=1,column=0,sticky = 'w',padx=10, pady=10)

label_email = Label(frame_principal,text='Correo : ')
label_email.grid(row=2,column=0,sticky = 'w',padx=10, pady=10)

label_password = Label(frame_principal,text='Password : ')
label_password.grid(row=3,column=0,sticky='w',padx=10,pady=10)

label_comentario = Label(frame_principal,text='Comentarios : ')
label_comentario.grid(row=4,column=0,sticky = 'w',padx=10, pady=10)


#creacion de los cuadros de texto
entry_nombre = Entry(frame_principal)
entry_nombre.grid(row=0,column=1,padx=10, pady=10)

entry_apellido = Entry(frame_principal)
entry_apellido.grid(row=1,column=1,padx=10, pady=10)

entry_email = Entry(frame_principal)
entry_email.grid(row=2,column=1,padx=10, pady=10)

entry_password = Entry(frame_principal)
entry_password.grid(row=3,column=1,padx=10, pady=10)
entry_password.config(show='*')

textocomentario = Text(frame_principal,width='15',height='8')
textocomentario.grid(row=4,column=1,padx=10,pady=10)

#crear un scroll
scrollvertical = Scrollbar(frame_principal,command=textocomentario.yview)
#se usa  sticky='nsew' para que se adapte a la acaja de Text
scrollvertical.grid(row=4,column=2,sticky='nsew')

#para que scroll se mueva conforme nos movemos por la caja de Text
textocomentario.config(yscrollcommand=scrollvertical.set)

root.mainloop()