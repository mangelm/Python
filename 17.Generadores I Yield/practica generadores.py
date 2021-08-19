#Funciones normal
def generaPares(limite):

    num = 1

    miLista = []

    while num<limite:

        miLista.append(num*2)

        num=num+1

    return miLista

print("Ejemplo funcion normal: ",generaPares(10))

#Modificado para generador
def generaPares(limite):

    num = 1

    while num<limite:

        yield num*2

        num = num +1

devuelvePares=generaPares(10)

for par in devuelvePares:
    print(par)

#Para imprimirmelos tres primeros elementos con el metodo next
print(next(devuelvePares))
print("Aqui podria haber mas codigo ...")
print(next(devuelvePares))
print("Aqui podria haber mas codigo ...")