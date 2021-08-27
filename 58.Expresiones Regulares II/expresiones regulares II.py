"""
Las expresiones regulares son una secuencua de caracteres que forman un patrón de busqueda

Sirven para el trabajo y procesamiento de texto
"""

import re

"""
lista_nombres=['Ana Gómez', 
                'María Martín', 
                'Sandra López',
                'Santiago Martíns',
                'Sandra Fernández']

for elemento in lista_nombres:
    #el ^ sirve para buscar los que empieza por lo que haya detras
    if re.findall('^Sandra',elemento):
        print(elemento)
"""

""" lista_nombres=['http://pildorasinformaticas.es', 
               'ftp://pildorasinformaticas.es', 
               'http://pildorasinformaticas.com',
               'ftp://pildorasinformaticas.com']

for elemento in lista_nombres:
    #en el caso de buscar los que terminen por el caracter de antes del dolar
    if re.findall('es$',elemento):
        print('Empiezan por el elemento elegido:',elemento)
    if re.findall('^ftp',elemento):
        print('Termina por el elemento escogido:',elemento)
 """
""" lista_nombres=['hombres',
               'mujeres',
               'mascotas',
               'niños',
               'niñas'
                ] """

""" for elemento in lista_nombres:
    #en el caso de buscar los que incluyan
    if re.findall('niñ[oa]s',elemento):
        print(elemento) """

lista_nombres=['hombres',
               'mujeres',
               'mascotas',
               'camión',
               'camion'
                ] 

for elemento in lista_nombres:
    #en el caso de buscar los que incluyan
    if re.findall('cami[oó]n',elemento):
        print(elemento)