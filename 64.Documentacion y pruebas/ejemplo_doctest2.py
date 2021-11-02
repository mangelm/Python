def compruebaMail(mailusuario):
    """
    La funcion compruebaMail evalua un mail
    recibido en busco de la @. Si tiene una @ 
    es correcto, si tiene mas de una @ es incorrecto
    si la @ estaal final es incorrecto

    >>> compruebaMail('juan@cursos.es')
    True

    >>> compruebaMail('juancursos.es@')
    False

    >>> compruebaMail('juancursos.es')
    False

    >>> compruebaMail('juan@cursos@.es')
    False
    """
    arroba=mailusuario.count('@')

    if(arroba!=1 or mailusuario.rfind('@')==(len(mailusuario)-1) or mailusuario.find('@')==0):
        return False

    else:
        return True

import doctest
doctest.testmod()