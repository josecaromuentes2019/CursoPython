from tkinter import *
import math


class Calculadora():
    
  
    numfilas=1
    numcolum=1
    bandera = False
    def pintaCalculadora(self):

        self.root = Tk()
        self.root.title('Calculadora')

        self.frame = Frame(self.root,bd=10)
        self.frame.config(bg='#333333')
        self.frame.pack()

        self.pintarPantalla()
        self.pintarBotones()
        self.root.mainloop()

    def pintarPantalla(self):
        self.frame2= Frame(self.frame,bd=13,relief='sunken')
        self.frame2.grid(row=1,column=1,columnspan=4)
        self.memoriaPantalla = Text(self.frame2,state='disabled',width=16,height=1,pady=5,bd=0)
        self.memoriaPantalla.pack()
        self.pantallatext = Text(self.frame2,width=16,height=1,pady=5,bd=0)
        self.pantallatext.insert(END,0)
        self.pantallatext.config(state='disabled')
        self.pantallatext.pack()
        #self.pantallatext.grid(row=1,column=1,columnspan=4)

    
    def pintarBotones(self):
        
        botones = ['CE','C','%','/','7','8','9','x','4','5','6','-','1','2','3','+','+/-','0','.','=']
        for i,valor in enumerate(botones):
            micolor='#7F7F7F'
            if i%4 == 0:
                self.numfilas+=1
                self.numcolum=1

            if i == 0 or i ==1 :
                micolor='#FF0000'

            
            self.crearBotones(valor,micolor).grid(row=self.numfilas,column=self.numcolum,pady=1,padx=1)
            self.numcolum +=1

    def crearBotones(self,tecla,micolor):

        self.btn=Button(self.frame,text=tecla)
        if tecla == '=':
            self.btn.config(bg=micolor,width=4,cursor='hand2',command=self.calcular)
        elif tecla == 'C':
            self.btn.config(bg=micolor,width=4,cursor='hand2',command=self.corregir)
        elif tecla == 'CE':
            self.btn.config(bg=micolor,width=4,cursor='hand2',command= lambda : self.corregir(True))
        elif tecla == '/' or tecla == '+' or tecla == '-' or tecla == 'x':
            self.btn.config(bg=micolor,width=4,cursor='hand2',command=lambda : self.usoMemoria(tecla))
        else:
            self.btn.config(bg=micolor,width=4,cursor='hand2',command=lambda : self.capturaTecla(tecla))
        return self.btn


    def capturaTecla(self,dato):
        self.pantallatext.config(state='normal')
        self.memoriaPantalla.config(state='normal')
        textopantalla = self.pantallatext.get('0.0',END)
        
        textopantalla = textopantalla[:-1]
       
        if textopantalla[0] == '0' and dato.isdigit():   
            self.corregir(True)
            self.pantallatext.config(state='normal')
        
        if self.bandera:
            self.pantallatext.delete('0.0',END)
            self.bandera =False
 
            

        self.pantallatext.insert(END,dato)
        self.pantallatext.config(state='disabled')
        

    def calcular(self):

        self.memoriaPantalla.config(state='normal')
        self.pantallatext.config(state='normal')
        resultado = self.memoriaPantalla.get('0.0',END)
        resultado = re.sub('x','*',resultado)
        resultado = resultado[:-2]
        self.pantallatext.delete('0.0',END)
        self.pantallatext.insert(END,eval(resultado))
        self.pantallatext.config(state='disabled')
        self.memoriaPantalla.config(state='disabled')
        print(eval('math.sqrt(4)'))

    def usoMemoria(self,valor):
       
        self.memoriaPantalla.config(state='normal')
        self.pantallatext.config(state='normal')
            
        textopantalla = self.pantallatext.get('0.0',END)
        textopantalla = textopantalla[:-1]
        textopantalla+=valor
        self.memoriaPantalla.insert(END,textopantalla)
        self.bandera = True
        self.calcular()


    def corregir(self,borra = False):
        self.pantallatext.config(state='normal')
        

        if borra :
            texto = ''
        else:
            texto = self.pantallatext.get('0.0',END)
            texto=texto[:-2]

        self.pantallatext.delete('0.0', END)
        self.pantallatext.insert(END,texto)
        self.pantallatext.config(state='disabled')
       

cal = Calculadora()
cal.pintaCalculadora()

