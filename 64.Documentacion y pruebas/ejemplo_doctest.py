def areaTriangulo(base,altura):

    """
    Calcula el area de un triangulo dado

    >>> areaTriangulo(3,6)
    'El área del triángulo es: 9.0'

    >>> areaTriangulo(4,5)
    'El área del triángulo es: 10.0'

    >>> areaTriangulo(9,3)
    'El área del triángulo es: 13.5'

    """

    return "El área del triángulo es: " +str((base*altura)/2)

#print(areaTriangulo(2,4))

import doctest
doctest.testmod()