"""
-Son diretorios donde se almacenan modulos relacioados entr si.
-Sirven para organizar y realizar los modulos
-Se crea un paquete crear una carpeta con el archivo __init__.py
"""
from calculos.calculos_generales import dividir

dividir(4,6)

#Para los subpaquetes tenemos que hacer lo siguiente
from calculos.basicos.operaciones_basicas import *

sumar(5,7)

from calculos.redondeo_potencia.redondeoypotencia import *

potencia(5,7)

from calculos.basicos.operaciones_basicas import dividir

dividir(5,7)