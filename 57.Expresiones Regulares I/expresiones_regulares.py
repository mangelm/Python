"""
Las expresiones regulares son una secuencua de caracteres que forman un patrón de busqueda

Sirven para el trabajo y procesamiento de texto
"""

import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

#print(re.search("aprender", cadena)) #el texto que buscamos, segundo parametro texto donde lo queremos buscar

textoBuscar="aprender"

textoEncontrado = re.search(textoBuscar,cadena)

""" if re.search(textoBuscar, cadena) is not None:

    print("He encontrado el texto")

else:

    print("No he encontrado el texto") """

print(textoEncontrado.start()) #Nos dice el num del caracter donde empieza a encontrar el texto, desde 0

print(textoEncontrado.end())

print(textoEncontrado.span()) #Lo mismo que los otros 2 a la vez y lo devuelve en una lista

textoBuscar2="Python"

print(len(re.findall(textoBuscar2,cadena)))