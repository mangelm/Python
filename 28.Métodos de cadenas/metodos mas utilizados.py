#Metodo upper() convierte en mayusculas todas las letras
cadena_de_texto = "hola como te llamas"
print(cadena_de_texto.upper())

#Metodo lower() convierte en minusculas todas las letras
print(cadena_de_texto.lower())

#Metodo capitalize() convierte la primera letra de la cadena
print(cadena_de_texto.capitalize())

#Metodo count() cuenta cuantas veces aperece una cadena,o letra,o conjunto de listas dentro del texto
print("Hay esta cantidad de letra indicada:",cadena_de_texto.count("o"))

#Metodo find() representa la posicion de un caracter o grupo de caracteres en un texto
print("La letra preguntada esta en la posicion:",cadena_de_texto.find("h"))

#Metodo isdigit() devuelve un true o false,si el valor es un numero o no
cadena_de_texto2 = "2"
print(cadena_de_texto2.isdigit())

#Metodo isalum() devuelve un true o false,si es alfanumerico
cadena_de_texto3 = "a2"
print(cadena_de_texto3.isalnum())

#Metodo isalpha() devuelve un true o false,si es alfanumerico
cadena_de_texto4 = "Hola"
print(cadena_de_texto4.isalnum())

#Metodo split() separa por palabras utilizando espacios
cadena_de_texto5 = "holacomotellamas"
print(cadena_de_texto5.split())

#Metodo strip() borra los espacios sobrantes al principio y al final
cadena_de_texto6 = "Hola como estas"
print(cadena_de_texto6.strip())

#Metodo replace() cambia una letra o palabra por otra dentro de un string
cadena_de_texto7 = "Hola como estas"
remplazo = "Pepe"
print(cadena_de_texto7.replace(cadena_de_texto7,remplazo))

#Metodo rfind() representa el indice de la posicion de un caracter contando desde el final
print(cadena_de_texto.rfind("Hola"))