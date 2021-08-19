class Coche():
    #Propiedades
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    #Comportamiento = metodo = que es capaz de hacer
    #Self el propio objeto perteneciente a la clase, se usa dentro de la clase
    def arrancar(self):
        self.enmarcha=True

    def estado(self):
        if(self.enmarcha):
            print("El coche esta en marcha")
        
        else:
            print("El coche esta parado")

#Objeto o instancia o ejemplar, estamos llamando a las caracteristicas del coche

miCoche = Coche()
print("*************Primer coche***************")
print("El lago del coche es: ",miCoche.largoChasis)
print("El coche tiene: ", miCoche.ruedas,"ruedas")
miCoche.arrancar()
miCoche.estado()

#Creamos el segundo objeto
miCoche = Coche()
print("*************Segundo coche***************")
print("El lago del coche es: ",miCoche.largoChasis)
print("El coche tiene: ", miCoche.ruedas,"ruedas")
miCoche.estado()
