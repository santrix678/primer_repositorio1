# Definimos las ciudades de Ecuador y las dimensiones
ciudades = ["Machala", "Guayaquil", "Loja"]
num_dias = 7  # Lunes a Domingo
num_semanas = 4

# Creamos una matriz 3D con temperaturas ficticias
import random
temperaturas = [[[random.randint(-10, 35) for _ in range(num_dias)] for _ in range(num_semanas)] for _ in range(len(ciudades))]

# Calculamos el promedio de temperaturas por ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f'Ciudad: {ciudad}')
    for semana in range(num_semanas):
        suma_temperaturas = 0
        for dia in range(num_dias):
            suma_temperaturas += temperaturas[i][semana][dia]
        promedio = suma_temperaturas / num_dias
        print(f'  Semana {semana + 1}: Promedio de Temperatura = {promedio:.2f}°C')
    print()  # Línea en blanco para separar los resultados de cada ciudad

    