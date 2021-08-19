from tkinter import *
from tkinter import filedialog


root=Tk()


def abreFichero():

    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros de Excel","*.xlsx"),
    ("Ficheros de texto","*.txt"),("Todos los ficheros","*.*"))) #Por defecto va a documentos, Con initialdir elegimos el directorio inicial desde donde buscar

    print(fichero)

Button (root, text="Abrir fichero", command=abreFichero).pack()


root.mainloop()