class Coche():
    #Propiedades
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    #Comportamiento = metodo = que es capaz de hacer
    #Self el propio objeto perteneciente a la clase, se usa dentro de la clase
    #Arranca y dice estado coche
    def arrancar(self):
        self.enmarcha=arrancamos

        if(self.enmarcha):
            print("El coche esta en marcha")
        
        else:
            print("El coche esta parado")

       def estado(self):
           print("El coche tiene", self.ruedas,"ruedas.Un ancho de",self.anchoChasis,"y un largo de",self.largoChasis)
 

#Objeto o instancia o ejemplar, estamos llamando a las caracteristicas del coche

miCoche = Coche()
print("*************Primer coche***************")

miCoche.arrancar(True)

miCoche.estado()

#Creamos el segundo objeto
miCoche2 = Coche()
print("*************Segundo coche***************")
miCoche2.arrancar(False)
miCoche2.estado()
