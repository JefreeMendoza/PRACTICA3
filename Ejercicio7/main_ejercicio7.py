''' Problema 7:
Desarrollar un módulo que contenga las siguientes funciones:
● Que genere 20 números enteros aleatorios entre 0 y 100 y devuelva una lista.
● Mostrar la lista obtenida por pantalla.
● Ordenar los valores de la lista y mostrarla por pantalla.
Luego crea un script main.py en el mismo directorio en el que deberás importar el módulo y
ejecutar las funciones.
Nota: utilizar el módulo “random” para generar un número aleatorio
'''
import generador_numeros

def main():
    try:
        lista_aleatoria = generador_numeros.generar_numeros_aleatorios()
        
        generador_numeros.mostrar_lista(lista_aleatoria)
        generador_numeros.ordenar_y_mostrar(lista_aleatoria)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()