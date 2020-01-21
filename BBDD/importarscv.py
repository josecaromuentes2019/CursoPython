
import sqlite3
import csv
 
#Abrimos el archivo CSV
f=open('C:/Users/JOSECARO/Downloads/city.csv','r') 
#Omitimos la linea de encabezado
next(f, None)
reader = csv.reader(f, delimiter=';')
 
#Crea la BD en la carpeta donde se encuentra el script
sql = sqlite3.connect('BBDD/Posiciones')
cur = sql.cursor()
 
#Creamos la tabla
cur.execute("CREATE TABLE posiciones (nombre INTEGER,dni VARCHAR)")

#crea una lista de listas con la informacion del csv
otraReader = []
for i in reader:
    otraReader.append(i[0].split(','))
    
   
#Llenamos la BD con los datos del CSV usando executemany para agregar un grupo de datos
cur.executemany("INSERT INTO posiciones VALUES (?, ?)", otraReader)

#Muestro las filas guardadas en la tabla
#sumar = cur.execute("SELECT count(dni) from posiciones")
#print(sumar.fetchall())

for row in cur.execute('SELECT * FROM posiciones'):
    print(row)
 
#Cerramos el archivo y la conexion a la bd
f.close()
sql.commit()
sql.close()