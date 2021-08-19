"""
-Estructuras que extraen valores de una funcion y se almacenan en objetos iterables (que se pueden recorrer)

-Estos valores se almacenan de uno en uno

-Cada vez que un generador almacena un valor, esta permanece en un estado pausado hasta que se solicita el siguiente.

Esta caracteristica es conocida como suspencion de estado
"""

#En vez de return utilizamos yield pero este nos devuelve el primer valor

"""
-Son mas eficientes que las funciones tradicionales 

-Muy utiles con listas de valores infinitos

-Determinados escenarios
"""
def generanumeros():
    numeros = [1,2,3]
    yield numeros