from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width="1200", height="600")
miFrame.pack()

cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10) #Divide como si fuera una tabla la ventana
cuadroNombre.config(fg="red",justify="right")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*") #Substituye el valor que ponga por un asterisco

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0,column=0, sticky="e", padx=10, pady=10) #padx padding eje horizontal, pady padding eje vertical

ApellidoLabel = Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=2,column=0,sticky="e", padx=10, pady=10) #Sticky para alinear como puntos cardinales 

DireccionLabel = Label(miFrame, text="Dirección:")
DireccionLabel.grid(row=3,column=0,sticky="e", padx=10, pady=10)

PassLabel = Label(miFrame, text="Password:")
PassLabel.grid(row=1,column=0,sticky="e", padx=10, pady=10)

raiz.mainloop()