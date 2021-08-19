"""
1.Creación
2.Apertura
3.Manipulación
4.Cierre
"""
from io import open

#Creamos archivo en modo lectura
archivo_texto = open("archivo.txt","r") #Nombre archivo y modo que queremos abrir

texto = archivo_texto.read() #Para que nos lea el contenido del archivo

archivo_texto.close()

print(texto)