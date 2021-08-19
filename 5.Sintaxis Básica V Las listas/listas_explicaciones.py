"""
Sintaxis

nombreLista=[elem1,elem2,elem3]

con el indice sabemos la posicion del elemento empezando con el indice 0
"""

miLista=["María","Pepe","Marta","Antonio"]
print(miLista)

"""
print(miLista[2])
print(miLista[7]) #Dara error porque no existe el limite
print(miLista[-2]) #Comienza a contar desde la inversa es decir desde el final
print(miLista[0:3]) #Le pedimos que nos muestre desde el primer indice y excluye el elemento final
print(miLista[:2]) #Muestra los primeros elementos
print(miLista[1:3])
print(miLista[2:]) #Le decimos que muestra desde ese elemento hasta el final
"""

#Agregar elementos al final de una lista
miLista.append("Sandra")
print(miLista)

#Agregar en la posicion que quedamos
miLista.insert(2,"Sandra") #Primero posicion, luego elemento
print(miLista)

#Varios elementos a una lista des como si concatenaramos varias listas
miLista.extend(["Sandra","Ana","Lucía"])
print(miLista)

#Para devolvernos el indice es decir la posicion de la lista utilizamos la siguiente funcion
print(miLista.index("Antonio")) #siempre nos devolvera el primer elemento repetido

#Puede saber si un elemento esta en la lista
print("Pepe" in miLista) #True si esta, False si no esta 

#Puede tener diferentes elementos 
miLista2=["María",5,True,78.55]
print(miLista2)

#Para eliminar elementos
miLista.remove("Ana")
print(miLista)

#Para eleminar el ultimo elemento de la lista
miLista.pop()
print(miLista)

#Podemos sumar listlas con el operador de sumas
miLista3=["Sandra","Lucia"]
miLista4=miLista+miLista3
print(miLista4)

#Con el operador multiplicar repetimos la lista varias veces
miLista4=["Sandra","Lucia"]*3
print(miLista4)