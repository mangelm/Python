from tkinter import *

root = Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu,tearoff = 0) #Para quitar la barra de los 3 puntitos
archivoMenu.add_command(label="Nuevo") #Para añadir un subelemento
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator() #Barra de separacion 
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")   



archivoEdicion=Menu(barraMenu,tearoff = 0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu,tearoff = 0)

archivoAyuda=Menu(barraMenu,tearoff = 0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de...")

barraMenu.add_cascade(label="Archivo",menu=archivoMenu) #Primero especificamos el texto que queremos que tenga el recuadro y luego el elemento al que nos referimos

barraMenu.add_cascade(label="Edición",menu=archivoEdicion)

barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas)

barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)

root.mainloop()