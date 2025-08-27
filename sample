def sumar_todos_los_numeros(ruta_archivo):
    try:
        # Abre el archivo en modo lectura con codificación UTF-8
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            numeros = []  # Lista para almacenar los números encontrados
            for linea in archivo:  # Itera sobre cada línea del archivo
                for palabra in linea.split():  # Divide la línea en palabras
                    if palabra.isdigit():  # Verifica si la palabra es un número
                        numero = int(palabra)  # Convierte la palabra a entero
                        numeros.append(numero)  # Agrega el número a la lista
                        #print(f"Número encontrado: {numero}")  # Imprime el número encontrado
            if numeros:  # Verifica si se encontraron números
                #suma_total = sum(numeros)  # Suma todos los números encontrados
                print(tareaNum(numeros))  # Imprime la suma total
                #print(f"La suma de todos los números encontrados es: {suma_total}")  # Imprime la suma total
            else:
                print("No se encontraron números en el archivo.")  # Mensaje si no se encontraron números
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no fue encontrado.")  # Mensaje de error si el archivo no se encuentra
    except IOError:
        print(f"Error: Ocurrió un problema al leer el archivo '{ruta_archivo}'.")  # Mensaje de error si ocurre un problema al leer el archivo

def tareaNum(numeros):
    suma = numeros[0] + numeros[1]
    producto = numeros[2] * numeros[3]
    return suma, producto

# Ejecución del programa
if __name__ == "__main__":
    # Especifica la ruta del archivo
    ruta = "ejercicio_1.txt"  # Cambia por la ruta de tu archivo

    # Llamada a la función para sumar todos los números
    sumar_todos_los_numeros(ruta)
