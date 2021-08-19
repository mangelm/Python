#Forma de encadenar varios excepts
def divide():

    try:
        
        op1=float(input("Introduce el primero numero: "))

        op2=float(input("Introduce el segundo numero: "))

        print("La division es " + str(op1/op2))

    except ValueError:

        print("El valor introducido es erroneo")
    
    except ZeroDivisionError:

        print("NO se puede dividir entre zero")
    
    finally: #Se ejecuta siempre si o si

        print("Calculo finalizado")

divide()

#En este caso no daria igual que tuviera el finally porque el programa caeria
def divide():

    try:

        op1=float(input("Introduce el primer numero: "))

        op2=float(input("Introduce el segundo numero: "))

        print("La division es: " + str(op1/op2))

    finally: #Se ejecutara si o si

        print("Calculo finalizado")

divide()

#Es un except generalizado poco recomendado
def divide():

    try:

        op1=float(input("Introduce el primer numero: "))

        op2=float(input("Introduce el segundo numero: "))

        print("La division es: " + str(op1/op2))

    except:

        print("Se ha producido un error")

divide()