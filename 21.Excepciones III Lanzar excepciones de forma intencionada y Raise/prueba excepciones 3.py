#Ejemplo de raise
def evaluaEdad(edad):

    if edad<0:
        raise TypeError("No se permiten edades negativas") #El error daria igual

    if edad<20:
        print("Eres muy joven")
    elif edad<40:
        print("Eres joven")
    elif edad<65:
        print("Eres maduro")
    elif edad<100:
        print("cuidate ...")

print(evaluaEdad(-15))

#Ejemplo con raiz cuadrada
import math

def calculaRaiz(num1):

    if num1<0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)

op1 = int(input("Introduce un numero: "))

try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Programa terminado")