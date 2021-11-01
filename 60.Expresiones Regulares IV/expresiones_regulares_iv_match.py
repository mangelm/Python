import re

#Buscar patrones dentro de una cadena de texto

nombre1="Sandra López"

nombre2="Antonio Gómez"

nombre3="sandra López"

nombre4="Jara López"

nombre5="Lara López"

cadena1="Jara López"

cadena2="546546546"

cadena3="a54654654"

"Funcion Match busca si hay coincidencias al comienzo de una cadena de texto"

""" if re.match("Sandra",nombre1):

    print("Hemos encontrado el nombre")

else:
    print("No lo hemos encontrado") """

"""
La función match distingue entre mayusculas y minusculas, ademas podemos añadir un tercer 
parametro """
""" if re.match("Sandra",nombre3): #sensible a lo explicado arriba

    print("Hemos encontrado el nombre")

else:
    print("No lo hemos encontrado") """

""" if re.match("Sandra",nombre3, re.IGNORECASE): #Ignora si es mayuscula o minuscula

    print("Hemos encontrado el nombre")

else:
    print("No lo hemos encontrado") """

""" if re.match(".ara",nombre5, re.IGNORECASE):

    print("Hemos encontrado el nombre")

else:
    print("No lo hemos encontrado") """

#Patrones busqueda python para mas info
""" if re.match("\d",cadena2): #\d se refiere a digito es exclusivo de python

    print("Hemos encontrado el número")

else:
    print("No lo hemos encontrado")
"""


 
