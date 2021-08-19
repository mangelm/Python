#Edad
edad = 7

if 0<edad<100: #Compara primero la primera parte y luego la segunda si no se cumple la primera
    print("Edad correcta")
else:
    print("Edad incorrecta")

#Evaluar salarios

salario_presidente=int(input("Introduce salario presidente: "))
print("Salario presidente: " + str(salario_presidente))

salario_director=int(input("Introduce salario director: "))
print("Salario director: " + str(salario_director))

salario_jefe_area=int(input("Introduce salario jefe area: "))
print("Salario Jefe Area: " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce salario administrativo: "))
print("Salario administrativo: " + str(salario_administrativo))

#Siempre va de izquierda a derecha es decir el if a los dos puntos
if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta empresa")