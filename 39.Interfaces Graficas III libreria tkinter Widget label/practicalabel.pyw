from tkinter import *

root=Tk()

miFrame = Frame(root,width=500,height=400)

miFrame.pack()

miLabel = Label(miFrame, text="Hola alumnos de Python", fg="red",font=("Comic Sans MS",18)).place(x="100",y="200")  #Añade un campo de texto al frame

#miLabel.pack() 

#miLabel.place(x="100",y="200") #Distancia del campo label, lo mismo largo

#miLabel = Label(miFrame, text="Hola alumnos de Python").place(x="100",y="200") abreviado
root.mainloop()

#Esta libreria trabajo con los formatos de imagen png,gif