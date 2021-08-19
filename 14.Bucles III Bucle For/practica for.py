#Empezamos la explicacion del range
#Crea una lista de 5 elementos
for variable in range(5):
    print("hola")

#Mismo ejemplo para que nos imprima la variable
for variable in range(5):
    print(variable)


#Para espicificar una funcion de tipo fm esto es del print´
for variable in range(5):
    print(f"valor de la variable {variable}")

#Para que nos cuente desde un numerohasta el anterior:
for rango in range(5,10):
    print(f"valor de la variable {variable}")

#De cuanto en cuanto lo indica el ultimo valor
for rango in range(5,50,3):
    print(f"valor de la variable {variable}")


#Para recorrer un email es correcto o no con len

valido = False

email = input("Introduce tu email:")

for arroba in range(len(email)):

    if email[variable]=="@":

        valido = True

if valido:
    print("Email correcto")

else:
    print("Email incorrecto")