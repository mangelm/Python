#Ejemplo de continue, ignorada una linea en concreto
for letra in "Python":

    if letra == "h":
        continue

    print("Viendo la letra: " + letra)

#Otro ejemplo
nombre = "Pildoras Informaticas"

contador = 0

for letras in nombre:

    if letras == " ":
        continue
    contador +=1

print(contador)