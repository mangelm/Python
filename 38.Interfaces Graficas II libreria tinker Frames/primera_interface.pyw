from tkinter import *

#Creamos la raiz con la classe tk y creamos la ventana
raiz=Tk()

raiz.title("Ventana de pruebas")

#raiz.resizable(0,0) #Uno corresponde al ancho y el otro al largo con 0,0 no se puede redimencionar, con un 1 en cualquiera redimencionas 

#raiz.iconbitmap("gato.ico") #Podemos cambiar el icono que se ve en la ventana con este comando,tenemos que tener una imagen .ico

#raiz.geometry("650x350") #Para cambiar el tamaño predeterminado de la ventana

raiz.config(bg="blue") #Con .config podemos cambiar cosas, bg es para backgroundcolor

raiz.config(bd=45) #Tamaño de borde

raiz.config(relief="sunken") #Para aplicar borde y buscar tipo de borde

raiz.config(cursor="pirate") #Cambiamos el tipo de cursor del raton

#construimos el frame y lo metemos dentro de la raiz
miFrame = Frame()

#miFrame.pack() #Necesario para empaquetar el frame

#miFrame.pack(side="right") #El frame queda anclado en la derecha

miFrame.pack(side="right",anchor="n") #El anchor te permite añadir otra direccion y funciona como los puntos cardinales, ahora seria arriba a la izquierda

miFrame.pack(fill="x") #Espande el eje x

miFrame.pack(fill="y", expand=True) #Para que se expande verticalmente

miFrame.pack(fill="both", expand=True) #Se expande hacia ambos lados

miFrame.config(bg="red")

miFrame.config(width="650",height="350")

miFrame.config(bd=35) #Tamaño de borde

miFrame.config(relief="groove") #Para aplicar borde y buscar tipo de borde

miFrame.config(cursor="hand2") #Cambiamos el tipo de cursor del raton

#Todo se puede ablicar a la raiz

raiz.mainloop() #Como un bucle infinito

#Cambiamos extension archivo pyw para que no nos abra la consola