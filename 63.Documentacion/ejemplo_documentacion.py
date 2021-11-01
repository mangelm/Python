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

#Nos imprime los comentarios de la funcion en concreto con .__doc__
print(areaCuadrado.__doc__) 

#Otra forma de imprimir los comentarios sin utilizar print
help(areaCuadrado) 
help(areaTriangulo)