#1. Abrir y crear conexión
import sqlite3

miconexion=sqlite3.connect("PrimeraBase")

#2.Crear Puntero
miCursor=miconexion.cursor()
#3.Ejecutar querry (consulta) SQL
#4.Manejar los resultados de la querry (consulta). 1.Insetar, leer, actualizar, borrar (Create, Read, Update, Delete)
miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))") #Si queremos añadir campos hay que comentar lo que ya este creado

miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")

miconexion.commit() #Para verificar los cambios
#5.Cerrar Puntero


#6.Cerrar conexión
miconexion.close()