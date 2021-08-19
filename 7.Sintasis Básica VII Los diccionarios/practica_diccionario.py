#Forma de escribir un diccionario
midiccionario = {}

#Diccionario lleno clave:valor
midiccionario={"Alemania:Berlín","Francia:París","Reino Unido:Londes","España:Madrid"}

#Para mostrar el valor asignado a una clave:
print(midiccionario["Alemania"])

#Acceder al diccionario entero
print(midiccionario)

#Agregar elementos a un diccionario
midiccionario["Italia"]="Lisboa"
print(midiccionario)
#Corregimos valor erroneo sobreescribimos
midiccionario["Italia"]="Roma"
print(midiccionario)

#Eliminar elementos del diccionario
del midiccionario["Reino Unido"]
print(midiccionario)

#Usar tupla para añadir a diccionario
mitupla=["España","Francia","Reino Unido","Alemania"]
midiccionario={mitupla[0]:"Madrid",mitupla[1]:"París",mitupla[2]:"Londres",mitupla[3]:"Berlín"}

#Meter una lista dentro de un dicionario
midiccionario{"Jordan":22,"Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":[1991,1992,1993.1996,1997,1998]}}
print(midiccionario)
print(midiccionario["equipos"])
print(midiccionario["anillos"])

#Obtener las claves del diccionario
print(midiccionario.keys())

#Obtener los valores de un diccionario
print(midiccionario.values())

#Obtener longitud diccionario
print(len(midiccionario))

