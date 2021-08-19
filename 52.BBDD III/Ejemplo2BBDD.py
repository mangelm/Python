import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()


""" miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''') #TRIPLE COMILLAS PARA DIVIDIR EN VARIAS LINEAS

productos=[

    ("AR01", "pelota", 20, "juguetería"),
    ("AR02", "pantalón", 15, "confección"),
    ("AR03", "destornillador", 25, "ferretería"),
    ("AR04", "jarrón", 45, "cerámica")
]
 """

# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

# miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05','tren',15,'juguetería')")

miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR03','tren',15,'juguetería')") #Peta porque el campo primario no se puede repetir

miConexion.commit()

miConexion.close()