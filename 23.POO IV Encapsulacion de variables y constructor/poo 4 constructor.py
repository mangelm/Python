class Coche():
    #Propiedades y constructor, este seria el estado inicial
    def __init__(self):

        self.largoChasis = 250
        self.anchoChasis = 120
        self.ruedas = 4
        self.enmarcha = False

    #Comportamiento = metodo = que es capaz de hacer
    #Que ademas de arrancar nos diga el "estado del coche"
    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos

        if self.enmarcha:
            print("El coche esta en marcha")
        else:
            print("El coche esta parado")

    def estado(self):
        print("El coche tiene",self.ruedas,"ruedas.Un ancho de",self.anchoChasis,"y un largo de",self.largoChasis)

#Objeto o instancia o ejemplar, estamos llamando a las caracteristicas del coche
miCoche = Coche()
print("**************Primer Coche**************")

miCoche.arrancar(True)
miCoche.estado()

#Segundo coche
miCoche2 = Coche()
print("***********Segundo coche**********")
miCoche2.arrancar(False)
miCoche2.estado()