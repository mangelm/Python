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
        
coche1 = vehiculos("Mazda","MX5")

coche2 = vehiculos("Seat","Leon")

coche3 = vehiculos("Renault","Megane")

coches=[coche1,coche2,coche3]

#Abrimos el fichero en escritura binario
fichero = open("losCoches","rb")

#Guardamos dentro del fichero los datos que queremos
pickle.dump(coches,fichero)
fichero.close()
del(fichero)

#Entocnes leemos el fichero en bites
ficheroApertura = open("losCoches","rb")
misCoches = pickle.load(ficheroApertura)
ficheroApertura.close()

#para recorrer la informacion
for coches in misCoches:

    print(coches.estado())