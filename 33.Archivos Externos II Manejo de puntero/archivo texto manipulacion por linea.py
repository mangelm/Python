from io import open

archivo_texto = open("archivo.txt","r+")

#Substituye tambien la primera linea del texto
lista_texto = archivo_texto.readlines()

lista_texto[1] = "Esta linea ha sido incluida desde el exterior\n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)