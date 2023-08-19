''' Problema 4:
Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y
ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los
atributos de la clase.
'''
import operacion_rec

def main():
    try:
        largo = float(input("Ingrese el largo del rectangulo: "))
        ancho = float(input("Ingrese el ancho del rectangulo: "))
        if largo < 0 and ancho < 0:
            print("Error: El radio debe ser un valor positivo.")
            return

        rectangulo = operacion_rec.Rectangulo(largo,ancho)
        area = rectangulo.calcular_area()
        print(f"El área del rectangulo con largo {largo} y ancho {ancho} es: {area:.2f}")

    except ValueError:
        print("Error: Ingrese un valor numérico válido.")

if __name__ == "__main__":
    main()
