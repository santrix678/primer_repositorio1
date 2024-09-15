# Definir una matriz 3x3 con valores numéricos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def buscar_valor(matriz, valor_a_buscar):
    """
    Busca un valor específico en la matriz y devuelve su posición.

    Args:
        matriz (list): La matriz bidimensional donde se realizará la búsqueda.
        valor_a_buscar (int): El valor que se desea buscar en la matriz.

    Returns:
        tuple: La posición (fila, columna) del valor encontrado o None si no se encuentra.
    """
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == valor_a_buscar:
                return (fila, columna)
    return None

# Definir el valor a buscar en la matriz
valor = 5

# Llamar a la función de búsqueda
posicion = buscar_valor(matriz, valor)

# Mostrar el resultado de la búsqueda
if posicion:
    print(f"Valor {valor} encontrado en la posición: fila {posicion[0]}, columna {posicion[1]}")
else:
    print(f"Valor {valor} no encontrado en la matriz.")


