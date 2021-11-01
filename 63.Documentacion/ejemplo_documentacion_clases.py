from Ejemplo_documentacion_modulos import *

class Areas:

    """
    Esta clase calcula las areas de diferentes figuras geometricas
    """
    def areaCuadrado(lado):

        """
        Calcula el area de un cuadrado
        elevando al cuadrado el lado pasado por parametro
        """

        return "El área del cuadrado es: " + str(lado*lado)

    def areaTriangulo(base,altura):

        """
        Calcula el area de un triangulo 
        utilizando los parametros base y altura
        """

        return "El área del triángulo es: " + str((base*altura)/2)

#Otra forma de imprimir los comentarios sin utilizar print
#help(Areas.areaTriangulo) 
#help(Areas)
help(Ejemplo_documentacion_modulos)