"""
Diferencia al posicionar con read o seek

Read: hasta donde le digamos
Seek: Desde donde le decimos
"""
from io import open

archivo_texto = open("archivo.txt","r")

print(archivo_texto.read(11))

print(archivo_texto.read()) #Desde la posicion siguiente a la anterior

#Para situar el cursor justo en medio del archivo de texto utilizamos lo siguiente
archivo_texto.seek(len(archivo_texto.readlines()))
print(archivo_texto.read())