import sqlite3
#import csv

#f=open('C:/Users/JOSECARO/Desktop/PRODUCTOS.csv','r') 

#next(f, None)
#reader = csv.reader(f, delimiter=';') 

sql = sqlite3.connect('BBDD/curso_sql')
cur = sql.cursor()
 
#Creamos la tabla
#cur.execute("""
#    CREATE TABLE productos (
#    CODIGOARTICULO INTEGER PRIMARY KEY AUTOINCREMENT,
#    SECCION VARCHAR(40),
#    NOMBREARTICULO VARCHAR (50),
#    PRECIO INTEGER,
#    FECHA VARCHAR(40),
#    IMPORTADO VARCHAR(10),
#    PAISORIGEN VARCHAR(50)
#    )""")


#cur.executemany("INSERT INTO productos VALUES (NULL,?,?,?,?,?,?)", reader)

#Muestro las filas guardadas en la tabla
#for row in cur.execute('SELECT * FROM productos'):
#   print(row)

#PRODUCTOS DE ESPAÑA
#sq = cur.execute("SELECT * FROM PRODUCTOS WHERE FECHA BETWEEN '2000-03-01' AND '2000-04-30' order by precio")
#sq = cur.execute("""SELECT * FROM PRODUCTOS WHERE SECCION = 'DEPORTES' OR SECCION = 'CERÁMICA' ORDER BY SECCION,paisorigen,precio""")
sq = cur.execute("SELECT SECCION, AVG(PRECIO) FROM PRODUCTOS WHERE SECCION='CONFECCIÓN' OR SECCION='DEPORTES' GROUP BY SECCION")
#sq = cur.execute("SELECT SECCION, PRECIO FROM  productos WHERE SECCION ='CONFECCIÓN' ORDER BY PRECIO DESC LIMIT 3 ")
pais = sq.fetchall()
for i in pais:
    print(i)

 
#Cerramos el archivo y la conexion a la bd
#f.close()
sql.commit()
sql.close()