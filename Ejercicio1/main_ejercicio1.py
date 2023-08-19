''' Problema 1:
Implemente un programa que solicite al usuario una fracción, con
formato X/Y, donde cada uno de X e Y es un número entero, y luego
muestra, como un porcentaje redondeado al número entero más
cercano, donde se indicará la cantidad de combustible en el
tanque. Se debe tener en cuenta los siguientes casos:
- Colocar E en caso X/Y sea menor a 1% del total
- Colocar F en caso X/Y sea mayor a 99%.
- En otro caso, devolver el valor en porcentaje %
También debe tomar en cuenta los siguientes casos:
- X y Y deben ser números enteros
- X debe ser mayor o igual a Y, y Y != 0
De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar
cualquier excepción como ValueError o ZeroDivisionError.
Ejemplos:
- Input: 4/0 Acción: Volver a preguntar al usuario dada la excepción ZeroDivisionError
- Input 1.5/3 Acción: Error dado que solo se permiten números enteros ValueError
- Input 5/4 Acción: Volver a preguntar al usuario
- Input 3/4 Output: 75%
- Input 4/4: Output F
Nota: Le será de utilidad aplicar
try:
...
except ValueError:
...
except ZeroDivisionError:
...

'''

## importo la operacion que calcula el porcentaje de combustible 
import operacion 

def main():
    while True:
        try:
            fraction = input("Ingrese una fracción en formato X/Y: ")
            x, y = map(int, fraction.split('/'))
            if x > y and y!=0:
                print("Error: X debe ser mayor o igual a Y.")
                continue

            result = operacion.calcular_combustible(x, y)
            print("Cantidad de combustible en el tanque:", result)
            ##break si quisiera que el programa ya no vuelva a preguntar 
        
        except ValueError:
            print("Error: Solo se permiten números enteros.")
            break
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            break
            
if __name__ == "__main__":
    main()