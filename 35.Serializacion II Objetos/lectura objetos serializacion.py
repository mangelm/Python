import pickle

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
        
ficheroApertura = open("losCoches","rb")

misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

#Para recorrer la informacion
for coches in misCoches:

    print(coches.estado())