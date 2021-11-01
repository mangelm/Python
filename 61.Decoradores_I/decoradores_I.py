#Los decodores añaden funcionalidades alr esto de programas
"""
Sintaxis:

def funcion_decorador(funcion):
    def funcion_internal():
        #codigo de la funcion interna
    return funcion_interna
"""
def funcion_decoradora(funcion_parametro):
    
    def funcion_interior():

        #Acciones adicionales que decoran

        print("Vamos a realizar un cálculo: ")

        funcion_parametro()

        #acciones adicionales que decoran

        print("Hemos terminado el cálculo")

    return funcion_interior


#funciones que queremos "decorar"
@funcion_decoradora #con esto le digo que decore esta funcion, encima de la funcion a decorar
def suma():
    print(15+20)

def resta():
    print(30-10)

suma()

resta()