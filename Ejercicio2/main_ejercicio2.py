''' Problema 2:
Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
formato. (Los métodos de cadena le serán de utilidad)
'''

def main():
    calificaciones_str = input("Ingrese las calificaciones separadas por comas: ")
    calificaciones_list = calificaciones_str.split(',')

    calificaciones_enteros = []

    for calificacion_str in calificaciones_list:
        try:
            calificacion = int(calificacion_str.strip())
            calificaciones_enteros.append(calificacion)
        except ValueError:
            print(f"Error: No se pudo convertir '{calificacion_str.strip()}' a un número entero.")

    print("Calificaciones enteras:", calificaciones_enteros)


main()