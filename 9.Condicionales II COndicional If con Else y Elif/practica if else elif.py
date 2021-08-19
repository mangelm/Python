#Controlaremos la edad del menor
print("Verificacion de acceso")

edad_usuario = int(input("Introduce tu edad porfavor:"))

if edad_usuario<18:
    print("No puedes pasar")
else:
    print("Puedes pasar")
print("El programa se ha finalizado")

#El else acompaña al if mas cercano
print("Verificacion de acceso")

edad_usuario = int(input("Introduce tu edad porfavor:"))

if edad_usuario<18:
    print("No puedes pasar")
elif edad_usuario>100:
    print("Edad incorrecta")
else:
    print("Puedes pasar")
print("El programa se ha finalizado")

#Introduce una nota, esto funciona en un solo bloque

print("Verificacion de acceso")

nota_usuario = int(input("Introduce tu nota porfavor:")

if nota_usuario<5:
    print("Insuficiente")

elif nota_usuario<6:
    print("Suficiente")

elif nota_usuario<7:
    print("Bien")

elif nota_usuario<9:
    print("Notable")

else:
    print("Sobresaliente")