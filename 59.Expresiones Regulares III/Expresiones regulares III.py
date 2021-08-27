"""
Las expresiones regulares son una secuencua de caracteres que forman un patrón de busqueda

Sirven para el trabajo y procesamiento de texto

Trabajar rangos
"""

import re

""" lista_nombres=['Ana',
               'Pedro',
               'María',
               'Rosa',
               'Sandra'
                ]  

for elemento in lista_nombres:
    #en el caso de buscar los que esten entre el rago separado con -
    if re.findall('[o-t]',elemento):
        print(elemento)                
                
                """

lista_nombres=['Ma1',
               'Se1',
               'Ma2',
               'Ba1',
               'Ma:3',
               'Va1',
               'Va2',
               'Ma4',
               'MaA',
               'Ma.5',
               'MaB',
               'Ma:C'
                ] 

for elemento in lista_nombres:
    #en el caso de buscar los que esten entre el rago separado con -
    if re.findall('Ma[0-3A-B]',elemento):
        print(elemento)