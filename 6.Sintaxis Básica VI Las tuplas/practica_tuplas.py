"""
Tupla mas rapida que una lista
NO se permiten añadir, eliminar, mover elementos
Si se permite extraer cachitos

nombreTupla = (elem1,elem2,elem3)
"""

#Para saber el elemento de una posicion de la tupla
mitupla=("Juan",13,1,1995)
print(mitupla[1])

#Convertir una tupla en una lista
mitupla=("Juan",13,1,1995)
milista=list(mitupla)
print(milista)

#Convertir una lista en una tupla
milista=["Juan",13,1,1995]
mitupla=tuple(mitupla)
print(mitupla)

#Comprobar elementos en la tubla
mitupla=("Juan",13,1,1995)
print("Juan" in mitupla)

#Saber cuantas veces hay un elemento en la tupla
mitupla=("Juan",13,1,1995)
print(mitupla.count(13))

#Longitud de la tupla
mitupla=("Juan",13,1,1995)
print(len(mitupla))

#Crear una tupla unitaria, es decir una tupla con un solo elemento
mituplaunitaria=("Juan",)
print(len(mitupla))

#Otra forma de crear una tupla mas conocido como empaquetado de tupla
mitupla="Juan",13,1,1995
print(mitupla)

#Desempaquetado de tupla
mitupla=("Juan",13,1,1995)
nombre, dia, mes, agno = mitupla
print(nombre)
print(dia)
print(agno)
print(mes)