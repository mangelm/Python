"""
-Veremos como recorrer strings(cadenas de texto)
-El tipo range (nos permite el conteo numerico)
-Notaciones especiales con print
"""
#Nos imprime cada elemento en un salto de linea por defecto
for variable in ["Pildoras","Informaticas",1]:
    print("¡Hola!")

#Si queremos que nos imprima todo en la misma linea:
for variable in ["Pildoras","Informaticas",1]:
    print("Hola",end="")
    #En este segundo print cada espacio que dejemos es un espacio mas
    print("Hola",end=" ")

#En el caso de una cadena de texto nos haria tantas veces como caracteres tenga la cadena:
for variable in "juan@pildorasinformaticas.com":
    print("Hola",end=" ")

#Evaluar si es correcta la direccion del correo
email = False

for arroba in "juan@pidorasinformaticas.com":

    if(arroba=="@"):
        email=True

if email==True:
    print("Email es correcto")
else:
    print("Email no correcto")

#Mismo ejemplo anterior simplificado
email = False

for arroba in "juan@pildorasinformaticas.com":

    if arroba == "@":
        email=True

if email:
    print("Email es correcto")
else:
    print("Email no correcto")

#Mismo ejemplo con introduccion de teclado
email = False
miemail = input("Introduce tu direccion de email")

for arroba in miemail:

    if arroba == "@":
        email=True

if email:
    print("Email es correcto")
else:
    print("Email no es correcto")

#Mismo ejemplo contemplando que tambien tenga punto
contador = 0
miemail = input("Introduce tu direccion de email")

for caracter in miemail:

    if caracter=="@" or caracter==".":
        contador = contador +1

if contador == 2:
    print("Email es correcto")
else:
    print("Email no es correcto")