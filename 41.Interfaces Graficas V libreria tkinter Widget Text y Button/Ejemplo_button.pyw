from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width="1200", height="600")
miFrame.pack()

minombre=StringVar() #Para decirle que es una variable de tipo texto

cuadroNombre = Entry(miFrame, textvariable=minombre) #Con textvariable asociamos la variable mi nombre a este campo
cuadroNombre.grid(row=0, column=1, padx=10, pady=10) #Divide como si fuera una tabla la ventana
cuadroNombre.config(fg="red",justify="right")

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*") #Substituye el valor que ponga por un asterisco

textoComentario = Text(miFrame, width=16,height=5) #Para añadir cuadros de texto, le añadimos nostros tamaño porque sino,tendria uno por defecto
textoComentario.grid(row=4,column=1, padx=10, pady=10)

scrollVert = Scrollbar(miFrame, command=textoComentario.yview) #Una barra de scroll que se mueve en el cuadro de texto
#Con el command decimos a quien pertenece y el eje, yview el eje vertical, xview el eje horizontal
scrollVert.grid(row=4,column=2,sticky="nsew") #Para que se adapte al tamaño que le tocaria, ponemos el sticky nsew que serian los 4 punts cardinales

textoComentario.config(yscrollcommand = scrollVert.set) #Para indicar en todo momento en que punto nos encontramos

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0,column=0, sticky="e", padx=10, pady=10) #padx padding eje horizontal, pady padding eje vertical

ApellidoLabel = Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=2,column=0,sticky="e", padx=10, pady=10) #Sticky para alinear como puntos cardinales 

DireccionLabel = Label(miFrame, text="Dirección:")
DireccionLabel.grid(row=3,column=0,sticky="e", padx=10, pady=10)

PassLabel = Label(miFrame, text="Password:")
PassLabel.grid(row=1,column=0,sticky="e", padx=10, pady=10)

ComentariosLabel = Label(miFrame, text="Comentarios:")
ComentariosLabel.grid(row=4,column=0,sticky="e", padx=10, pady=10)

def CodigoBoton():

    minombre.set("Juan")


botonEnvio=Button(raiz,text="Enviar",command=CodigoBoton) #Para crear el botton, con el command llamamos a la funcion del boton

botonEnvio.pack()

raiz.mainloop()