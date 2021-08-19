from tkinter import *

#Creamos la raiz con la classe tk y creamos la ventana
raiz=Tk()

raiz.title("Ventana de pruebas")

raiz.resizable(0,0) #Uno corresponde al ancho y el otro al largo con 0,0 no se puede redimencionar, con un 1 en cualquiera redimencionas 

raiz.iconbitmap("gato.ico") #Podemos cambiar el icono que se ve en la ventana con este comando,tenemos que tener una imagen .ico

raiz.geometry("650x350") #Para cambiar el tamaño predeterminado de la ventana

raiz.config(bg="blue") #Con .config podemos cambiar cosas, bg es para backgroundcolor

raiz.mainloop() #Como un bucle infinito

#Cambiamos extension archivo pyw para que no nos abra la consola