#Evaluacion si tiene derecho a beca
print("Programa de becas año 2020")

distancia_escuela=int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el nº de hermanos en el centro: "))
print(numero_hermanos)

salario_familiar=int(input("INtroduce salario anual bruto: "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
    print("Tiene derecho a becas")
else:
    print("No tienes derecho a becas")
#And igual a y

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
    print("Tienes derecho a becas")
else:
    print("No tienes derecho a becas")
#Or o si no´

#Programa para cursar asignatura optativa
print("Asignaturas Optativas Año 2020")
print("Asignaturas optativas: Informatica grafica - prueba de software - Usuabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida:")
asignatura = opcion.lower()

if asignatura in ("Informatica grafica","prueba de software","usabilidad y accesibilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print("La asignatura escogida no esta contemplada")