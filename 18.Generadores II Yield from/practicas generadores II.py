#De esta forma le decimos que lo recibira en forma de tupla
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield elemento

ciudades_devueltas = devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

#Ejemplo de sacar sub elemento
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        for subelemento in ciudades:
            yield subelemento

ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

#Con yield from es como si hicieramos un bucle for aninado
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento

ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))