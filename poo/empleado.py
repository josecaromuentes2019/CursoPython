import persona

class Empleado(persona.Persona):
    def __init__(self,salario,antigüedad,nombre,edad,identificacion):
        self.salario = salario
        self.antiüedad = antigüedad
        super().__init__(nombre,edad,identificacion)

    def descripcion(self):
        super().descripcion()
        print('Salario: ',self.salario,' Euros\nAntiguedad: ',self.antiüedad,' Años')
    
obj = Empleado(2000,15,'joose',32,234244)
obj.descripcion()