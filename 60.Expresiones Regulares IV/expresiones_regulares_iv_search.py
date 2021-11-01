import re

nombre1="Jara López"

nombre2="Antonio Gómez"

nombre3="Lara López"

codigo1="dsadsadasdasds71dasdasdsd"

codigo2="asdasd71dasdasdasdasdad"

codigo3="sasd asdasd dsadsd dsadsa dasda"

#Función Search busca en toda la cadena de texto para ver si se encuentra el patrón que buscamos
""" if re.search("López",nombre1): 

    print("Hemos encontrado el nombre")

else:
    print("No lo hemos encontrado") """

if re.search("71",codigo1): 

    print("Hemos encontrado el número")

else:
    print("No lo hemos encontrado")

