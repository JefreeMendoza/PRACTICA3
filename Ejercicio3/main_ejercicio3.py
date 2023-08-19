''' Problema 3:
Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
“CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio.
'''

import operacion_circulo

def main():
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        if radio < 0:
            print("Error: El radio debe ser un valor positivo.")
            return

        circulo = operacion_circulo.Circulo(radio)
        area = circulo.calcular_area()
        print(f"El área del círculo con radio {radio} es: {area:.2f}")

    except ValueError:
        print("Error: Ingrese un valor numérico válido.")

if __name__ == "__main__":
    main()