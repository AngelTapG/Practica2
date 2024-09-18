import random
import time


def generar_datos(alumnos, materias):
    # Crear una lista de listas para representar la matriz de alumnos y materias matriz = [[random.randint(0, 100) for _ in range(materias)] for _ in range(alumnos)]
    return matriz


def buscar_alumno_materia(matriz, alumno, materia):
    return matriz[alumno][materia]


def prueba_busqueda(alumnos, materias):
    print(f"\nPrueba con {alumnos} alumnos y {materias} materias:")

    
    matriz = generar_datos(alumnos, materias)
    
    
    try:
        alumno = int(input(f"Introduce el número del alumno (1 a {alumnos}): "))
        materia = int(input(f"Introduce el número de la materia (1 a {materias}): "))

        
        if alumno > alumnos or materia > materias or alumno <= 0 or materia <= 0:
            print("¡Entrada inválida! Asegúrate de ingresar un número dentro del rango.")
            return

      
        start_time = time.time()
        resultado = buscar_alumno_materia(matriz, alumno - 1, materia - 1)
        end_time = time.time()
        
        print(f"Resultado (alumno {alumno}, materia {materia}): {resultado}")
        print(f"Tiempo de ejecución: {end_time - start_time:.10f} segundos")

    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")


prueba_busqueda(500, 6)