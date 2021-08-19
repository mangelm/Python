#La posicion por defecto al abrir se pone al principio
from io import open

archivo_texto = open("archivo.txt","r")

print(archivo_texto.read())

#Despues de terminar de leer la posicion es la ultima asi que no muestra nada
#Con el metodo este nos pide la posicion donde queremos que se situe
archivo_texto.seek(0)

print(archivo_texto.read())