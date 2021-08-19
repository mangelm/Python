import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()


""" miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

productos=[

    ("pelota", 20, "juguetería"),
    ("pantalón", 15, "confección"),
    ("destornillador", 25, "ferretería"),
    ("jarrón", 45, "cerámica"),
    ("pantalones", 35, "confección")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos) """

""" # miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05','tren',15,'juguetería')")

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección'") #Asi realizamos consulta

productos=miCursor.fetchall() #Para que nos muestre todo

print(productos)
 """


""" #Hacer un update

miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO = 'pelota'") """

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 5")

miConexion.commit()

miConexion.close()