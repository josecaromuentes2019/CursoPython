class Persona():
    def __init__(self,nombre,edad,identificacion):
        self.nombre = nombre
        self.edad = edad
        self.identificacion = identificacion
    
    def descripcion(self):
        print('Nombre: ',self.nombre,'\nEdad: ',self.edad,' Años',
        '\nIdentificacion: ',self.identificacion)