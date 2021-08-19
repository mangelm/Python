class vehiculos():
    #Caracteristicas
    def __init__(self,marca,modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    #Comportamiento

    def arrancar(self):

        self.enmarcha = True
    
    def acelerar(self):

        self.acelera = True

    def frenar(self):

        self.frena = True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\En marcha:",self.enmarcha,"\nAcelerando:",self.acelera,"\nFrenando:",self.frena)

#Sintaxis para hererar

class Furgoneta(vehiculos):
    
    def carga(self,cargar):

        self.cargado = cargar

        if self, self.cargado:
            print("La furgoneta está cargado")
        
        else:
            print("La furgoneta no está cargado")

class Moto(vehiculos):

    hcaballito = ""

    def caballito(self):

        self.hcaballito = "Voy haciendo el caballito"

    def estado(self):

        print("Marca:",self.marca,"\nModelo:",self.modelo,"\nEn marcha:",self.enmarcha,"\Acelerando:",self.acelera,"\nFrenando:",self.frena,"\n",self.hcaballito) #Sobreescribimos el metodo estado

class VElectricos():
    
    def __init__(self):
        self.autonomia = 100

    def CargarEnergia(self):

        self.cargado=True

miMoto = Moto("Honda","CBR")

miMoto.estado()

mifurgoneta.estado()

mifurgoneta.carga(True)

#Herencia multiple, hereda el constructor de la primera herencia
class BicicletaElectrica(VElectricos,vehiculos):
    pass

miBici = BicicletaElectrica()