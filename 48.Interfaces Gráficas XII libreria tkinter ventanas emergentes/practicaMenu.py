from tkinter import *
from tkinter import messagebox

root = Tk()

#Constreye la ventana emergente
def infoAdicional(): #Ventana de información
    messagebox.showinfo("Procecesador de Angel","Procesador de textos version 2021") #El primero es el texto en el primer lugar

def avisoLicencia(): #Venta de aviso
    messagebox.showwarning("Licencia","Producto bajo licencia GNU")

def salirAplicacion():
    #valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?") #Para almecenar el valor de yes o no 
    valor=messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?") #Para almacenar el valor true o false
    
    """
    if valor=="yes":
        root.destroy() #Para cerrar la aplicacion en caso de que si
    """
    if valor==True: 
        root.destroy()

def cerrarDocumento():
    valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")
    if valor==False: 
        root.destroy()

        
#Para crear el menu y los submenus
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu,tearoff = 0) #Para quitar la barra de los 3 puntitos
archivoMenu.add_command(label="Nuevo") #Para añadir un subelemento
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator() #Barra de separacion 
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)   



archivoEdicion=Menu(barraMenu,tearoff = 0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu,tearoff = 0)

archivoAyuda=Menu(barraMenu,tearoff = 0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)


barraMenu.add_cascade(label="Archivo",menu=archivoMenu) #Primero especificamos el texto que queremos que tenga el recuadro y luego el elemento al que nos referimos

barraMenu.add_cascade(label="Edición",menu=archivoEdicion)

barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas)

barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)

root.mainloop()