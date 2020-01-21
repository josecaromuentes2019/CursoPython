import sqlite3
#conexion a la base si no existe la crea
miConenxion = sqlite3.connect("BBDD/miBase")

micursor = miConenxion.cursor()
#crear un atabla
#micursor.execute("CREATE TABLE productos(nombrearticulo varchar(50), precio integer, seccion varchar(20))")

#insertar un unico registro
#micursor.execute("INSERT INTO PRODUCTOS VALUES ('BALON',1500,'DEPORTES')")

#insertar un lote de registros
#misProductos = [
#    ("Cmiseta",23000,"Deportes"),
#    ('Camion',12000,'Jugueteria'),
#    ('Jarron',10000,'Ceramica')
#]
#micursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",misProductos)

#seleccionar registros
micursor.execute("SELECT * FROM PRODUCTOS")
misProductos = micursor.fetchall()

for var in misProductos:
    if var[1]>15000:
        for i in var:
            print(i)
            
miConenxion.commit()
miConenxion.close()