import funciones_matematicas

funciones_matematicas.sumar(7,5)

#Para usar una funcion en concreto
from funciones_matematicas import sumar
sumar(7,5)

#Para importar todo lo que tenemos en el otro archivo,esto es lo que hace es reservar espacio en la memoria
from funciones_matematicas import *
sumar(7,5)