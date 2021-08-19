def suma():
    num1=5
    num2=7
    print(num1+num2)

suma()

def suma_parametros(num1,num2):

    print(num1+num2)

suma_parametros(5,7)
suma_parametros(2,5)
suma_parametros(35,358)


def suma_return(num1,num2):

    resultado=num1+num2

    return resultado

print(suma_parametros(5,7))
print(suma_parametros(2,5))
print(suma_parametros(35,358))