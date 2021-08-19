import pickle

class Persona(): #Cada persona con sus caracteristicas

    def __init__(self,nombre,genero,edad): #Constructor para que siempre tenga esto de base
        
        self.nombre = nombre
        self.genero = genero
        self.edad = edad

    def __str__(self): #Simplemenente personalizados como queremos que nos lo muestre

        return "{} {} {}".format(self.nombre,self.genero,self.edad)

class ListaPersonas(): #para almacenar todas las personas

    personas=[]

    def __init__(self):#Constructor para agregar información a un fichero

        ListaDePersonas = open("ficheroExterno","ab+")#lo abrimos de forma append y binaria
        ListaDePersonas.seek(0) #Asegurarse que este en el principio

        try: #Con esto nos aseguramos que en caso de que este vacio de el print no falle el programa
            self.personas = pickle.load(ListaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        
        except:
            print("El fichero esta vacio")

        finally: #Para que haga las acciones entre o no en el fichero
            ListaDePersonas.close()
            del(ListaDePersonas)

    #Metodo para guardar las personas en una lista
    def agregarPersonas(self.persona):

        self.personas.append(personas)
        self.guardarPersonasEnFicheroExterno()

    #Con esto nos recorremos la lista y mostramos cada persona
    def mostrarPersonas(self):
        for persona in self.personas:
            print(persona)

    #Con abrimos el archivo en modo escritura y binario y guardamos la informacion en el fichero
    def guardarPersonasEnFicheroExterno(self):
        ListaDePersonas = open("ficheroExterno","wb")
        pickle.dump(self.personas,ListaDePersonas)
        ListaDePersonas.close()
        del(ListaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente:")
        for persona in self.personas:
            print(persona)

#Creamos un objeto de tipo lista y vamos almacenando las personas mediante el metodo creado anteriormente
miLista=ListaPersonas()
persona=Persona("Sandra","Femenino",29)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()