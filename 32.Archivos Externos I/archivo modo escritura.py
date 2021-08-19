"""
1.Creación
2.Apertura
3.Manipulación
4.Cierre
"""
from io import open

#Creamos archivo en modo escritura
archivo_texto = open("archivo.txt","w") #Nombre archivo y modo que queremos abrir
frase="Estupendo dia para estudiar Python \n el miercoles"

#Añadimos el contenidode la variable a la frase del archivo
archivo_texto.write(frase)

archivo_texto.close()