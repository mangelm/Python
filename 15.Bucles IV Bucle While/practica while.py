#Ejemplo de while
variable = 1

while variable<=10:
    print("Ejecucion " + str(variable))
    variable = variable + 1

print("Termino la ejecucion")

#Ejemplo de edad
edad = int(input("Introduce la edad porfavor:"))

while edad<0:
    print("Has introducido una edad negativa. VUelve a intentarlo")
    edad = int(input("Introduce la edad porfavor:"))

print("Gracias por colaborar.Puede pasar")
print("Edad del aspirante " + str(edad))

#Edad mas preciso
edad = int(input("Introduce la edad porfavor:"))

while edad<0 or edad>100:
    print("Has introducido una edad negativa.Vuelve a intentarlo.")
    edad = int(input("Introduce la edad porfavor"))

print("Gracias por colaborar.Puede pasar")
print("Edad del aspirante " + str(edad))

#Hacer que este bucle no sea infinito
import math

print("Programa de calculo de raiz cuadrada")
numero = int(input("Introduce un numero porfavor"))

intentos = 0

while numero<0:
    print("No se puede hallar la raiz de un numero negativo")

    if intentos == 2:
        print("Has consumido demasiados intentos.El programa ha finalizado")
        break; #No utilizar

    numero = int(input("Introduce un numero porfavor"))
    if numero<0:
        intentos = intentos + 1

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + "es" + str(solucion))