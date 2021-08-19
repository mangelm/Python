from tkinter import *

root=Tk()

varOpcion=IntVar()

def imprimir():

    #print(varOpcion.get()) #Obtener el valor de la opcion escogida

    if varOpcion == 1:

        etiqueta.config(text="Has elegido masculino")

    elif varOpcion == 2:

        etiqueta.config(text="Has elegido feminino")

    else:

        etiqueta.config(text="Has elegido otros")


Label(root, text="Género:").pack()

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack() #Primero donde esta ubicado el boton y luego el texto

Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack() #Asignandoles valores enteros hacemos que se deseleccione

Radiobutton(root, text="Otras opciones", variable=varOpcion, value=3, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()