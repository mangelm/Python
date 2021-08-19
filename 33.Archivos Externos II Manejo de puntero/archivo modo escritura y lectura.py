from io import open

archivo_texto = open("archivo.txt","r+")

#Substituye tambien la primera linea del texto
archivo_texto.write("Comienzo del texto")

print(archivo_texto.readlines())