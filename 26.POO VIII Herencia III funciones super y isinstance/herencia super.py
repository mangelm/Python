class persona():

    def __init__(self,nombre,edad,lugar_residencia):

        self.nombre = nombre

        self.edad = edad
        
        self.lugar_residencia = lugar_residencia

    def descripcion(self):

        print("Nombre:",self.nombre,"Edad:",self.edad,"Residencia:",self.lugar_residencia)

class Empleado(persona):

    def __init__(self,salario,antiguedad,edad_empleado,lugar_residencia): 

        #Esta llamando al metodo de la clase padre en este caso al metodo init de persona
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)

        self.salario = salario

        self.antiguedad = antiguedad

    def descripcion(self):

        super().descripcion()

        print("Salario:",self.salario,"Antiguedad:",self.antiguedad)

Manuel = persona(1500,15,"Manuel",55,"Colombia")

Manuel.descripcion()