from io import open

archivo_texto = open("archivo.txt","r") #Nombre archivo y modo que lo queremos abrir

#Para leer las lienas del texto en una lista
lineas_texto = archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto)

#Para acceder a los elementos del documento:
print(lineas_texto[0])
print(lineas_texto[1])