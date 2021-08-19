#Ejemplo con email

email = input("Introduce tu email,por favor: ")

for arroba in email:

    if arroba == "@":

        arroba=True

        break;

else:

    arroba=False

print(arroba)