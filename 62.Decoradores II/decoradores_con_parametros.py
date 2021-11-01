#Los decoradores añaden funcionalidades al resto de programas
"""
Sintaxis:

def funcion_decorador(funcion):
    def funcion_internal():
        #codigo de la funcion interna
    return funcion_interna
"""
def funcion_decoradora(funcion_parametro):
    
    def funcion_interior(*args, **kwargs): #args para un numero indeterminado de parametros , kwargs son argumentos con clave y valor

        #Acciones adicionales que decoran

        print("Vamos a realizar un cálculo: ")

        funcion_parametro(*args, **kwargs)

        #acciones adicionales que decoran

        print("Hemos terminado el cálculo")

    return funcion_interior

@funcion_decoradora
def suma(num1,num2,num3):

    print(num1+num2+num3)

@funcion_decoradora
def resta(num1,num2):

    print(num1-num2)

@funcion_decoradora
def potencia(base,exponente):

    print(pow(base,exponente))


suma(7,5,8)

resta(12,10)

potencia(base=5,exponente=3)