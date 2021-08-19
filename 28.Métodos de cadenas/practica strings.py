#Ejemplo simple
nombreUsuario = input("Introduce tu nombre de Usuario: ")

print("El nombre es:", nombreUsuario.upper())
print("El nombre es:", nombreUsuario.lower())
print("El nombre es:", nombreUsuario.capitalize())

#Ejemplo mas elaborado
edad = input("Introduce tu edad:")

while edad.isdigit() == False:
    
    print("Porfavor, introduce un valor numérico")
    edad = input("Introduce la edad:")

if int(edad)<18:

    print("No puede pasar")

else:

    print("Puede pasar")