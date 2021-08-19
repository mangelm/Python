#Si la condicion es verdadera se ejecutaba lo de dentro del if
def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(4))
print(evaluacion(5))

#Con introduccion por teclado

nota_alumno = int(input())

def evaluacion2(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print(evaluacion2(nota_alumno))