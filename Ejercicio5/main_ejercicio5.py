''' Problema 5:
Cree una clase Alumno e inicialícela con el nombre y el número de registro. Haga los métodos
para:
1. Display - Debe mostrar toda la información del estudiante (nombre y número de
registro).
2. setAge - Debe asignar la edad al estudiante
3. setNota - Debe asignar las notas al estudiante.
'''
import operacion_alumno

def main():
    nombre = input("Ingrese el nombre del estudiante: ")
    numero_registro = input("Ingrese el número de registro del estudiante: ")
    
    alumno = operacion_alumno.Alumno(nombre, numero_registro)

    while True:
        edad = input("Ingrese la edad del estudiante: ")
        try:
            alumno.setAge(edad)
            break
        except ValueError as e:
            print(e)

    while True:
        notas_str = input("Ingrese las notas separadas por comas: ")
        notas_list = notas_str.split(',')
        try:
            alumno.setNota(notas_list)
            break
        except ValueError as e:
            print(e)

    alumno.display()

if __name__ == "__main__":
    main()
