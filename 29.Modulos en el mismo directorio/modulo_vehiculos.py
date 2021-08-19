class vehiculos():
    #Caracteristicas                    
    def _init_(self, marca, modelo):

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    #Comportamiento
    
    def arrancar(self):

        self.enmarcha=True

    def acelerar(self):

        self.acelara=True

    def frenar(self):

        self.frena=True
        
    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenando:", self.frena)

#Sintaxis para hererar

class Furgoneta(vehiculos):

    def carga(self, cargar):

        self.cargado = cargar
        if(self, self.cargado):
            print("La furgoneta está cargada")

        else:
            print("La furgoneta no está cargada")

class Moto(vehiculos):
    hcaballito = ""
    
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenando:", self.frena, "\n", self.hcaballito) #Sobre escribimos el metodo estado

class VElectricos(vehiculos):
    def _init_(self,marca,modelo):
        
        super()._init_(marca, modelo)

        self.autonomia=100

    def CargarEnergia(self):

        self.cargado = True

#Herencia multiple hereda del constructor la primera herencia si esta repetido el nombre
class BicicletaElectrica(VElectricos,vehiculos):
    pass