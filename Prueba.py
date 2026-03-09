print("Hola cursor")

# Este bucle imprime los números del 0 al 4 en pantalla
for i in range(5):
    print(i)

edad = 18


def sumar(a, b, c):
    return "La suma es: " + str(a + b + c)

print(sumar(30, 50,10))


primos = []
for num in range(2, 100):
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(num)

print("Números primos menores de 100:", primos)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

"""
Esta función recibe una lista de números y devuelve la suma de los elementos de la lista.
@param lista: list - La lista de números a sumar.
@return total: int - La suma de los elementos de la lista.
@precondiciones: La lista debe ser una lista de números.
@postcondiciones: La suma de los elementos de la lista es devuelta.
def test_sumaLista():
    assert sumaLista([1, 2, 3, 4, 5]) == 15
    assert sumaLista([1, 2, 3, 4, 5]) == 15
"""

def sumaLista(lista:list):
    total = 0
    for elemento in lista:
        total += elemento
    return total

print(sumaLista([1, 2, 3, 4, 5]))

