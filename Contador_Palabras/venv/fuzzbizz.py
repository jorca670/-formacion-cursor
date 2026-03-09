# Puedes crear un archivo README.md para describir tu proyecto, por ejemplo:
        # 
        # # Contador de Palabras y FizzBuzz
        # 
        # Este proyecto contiene scripts en Python para contar palabras y para el clásico problema FizzBuzz.
        # 
        # ## Estructura del proyecto
        # - `fuzzbizz.py`: Implementación del problema FizzBuzz.
        # - Otros scripts relacionados con manipulación de textos o cálculo de cuadrados.
        #
        # ## Uso
        # Ejecuta cualquiera de los scripts para ver los resultados por consola.
        #

for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:

        print(i)