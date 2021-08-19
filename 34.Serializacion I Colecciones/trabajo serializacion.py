#Importamosla libreria pickle
import pickle

lista_nombres=["Pedro","Ana","Maria","Isabel"]

#Creamos fichero externo y lo abrimos en escritura binaria
fichero_binario = open("lista_nombres","wb")
#Lo que queremos guardar y donde lo queremos guardar
pickle.dump(lista_nombres,fichero_binario)
fichero_binario.close()

#del(fichero_binario) para eliminar el fichero

"""
Para leer la información del fichero hacemos lo siguiente
"""
fichero = open("lista_nombres","rb")
lista = pickle.load(fichero)

print(lista)