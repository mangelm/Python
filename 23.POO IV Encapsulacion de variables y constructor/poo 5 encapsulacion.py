class Coche():
    #Propiedades y constructor, este seria el estado inicial
    def __init__(self):

        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 #Encapsulado con dos guiones bajos que sirve para proteger una caracteristica y que sea fija
        self.__enmarcha = False

    #Comportamiento = metodo = que es capaz de hacer
    #Que ademas de arrancar nos diga el "estado del coche"
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos

        if self.__enmarcha:
            print("El coche esta en marcha")
        else:
            print("El coche esta parado")

    def estado(self):
        print("El coche tiene",self.__ruedas,"ruedas.Un ancho de",self.__anchoChasis,"y un largo de",self.__largoChasis)

#Objeto o instancia o ejemplar, estamos llamando a las caracteristicas del coche
miCoche = Coche()
print("**************Primer Coche**************")

miCoche.arrancar(True)
miCoche.estado()

#Segundo coche
miCoche2 = Coche()
print("***********Segundo coche**********")
miCoche2.arrancar(False)
miCoche2.__ruedas = 5
miCoche2.estado()