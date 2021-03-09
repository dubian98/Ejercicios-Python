nota_alumno = input("introduce la nota del alumno")

def evaluar(nota):
    valoracion ="aprobado"
    if nota < 5:
        valoracion = "suspendido"
    return valoracion 

evaluar(int(nota_alumno))
