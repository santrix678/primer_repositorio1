def promedio_temperatura(temperaturas, ciudades, semanas=None):
    # Inicializa un diccionario para almacenar los promedios por ciudad
    promedios_ciudades = {}

    # Verifica cuántas semanas hay disponibles en los datos
    num_semanas = len(temperaturas[0])  # Se asume que todas las ciudades tienen el mismo número de semanas
    num_dias = len(temperaturas[0][0])  # Se asume que todas las semanas tienen el mismo número de días

    # Si no se especifica el número de semanas, se calculan todas las disponibles
    if semanas is None or semanas > num_semanas:
        semanas = num_semanas

    # Recorre todas las ciudades para calcular sus promedios
    for i, ciudad in enumerate(ciudades):
        suma_total = 0
        dias_totales = semanas * num_dias

        # Suma todas las temperaturas de las semanas especificadas para cada ciudad
        for semana in range(semanas):
            for dia in range(num_dias):
                suma_total += temperaturas[i][semana][dia]

        # Calcula el promedio para la ciudad
        promedio = suma_total / dias_totales
        promedios_ciudades[ciudad] = promedio

    return promedios_ciudades

# Ejemplo de uso con los datos ficticios de ciudades
ciudades = ["Machala", "Guayaquil", "Loja"]
num_dias = 7  # Lunes a Domingo
num_semanas = 4

# Generamos las temperaturas ficticias para el ejemplo
import random
temperaturas = [[[random.randint(-10, 35) for _ in range(num_dias)] for _ in range(num_semanas)] for _ in range(len(ciudades))]

# Calcular el promedio de temperatura de las ciudades para un período de 3 semanas
resultado = promedio_temperatura(temperaturas, ciudades, semanas=3)
print("Promedio de temperatura por ciudad durante 3 semanas:")
for ciudad, promedio in resultado.items():
    print(f'{ciudad}: {promedio:.2f}°C')

# También puedes calcular para todas las semanas si no pasas el parámetro semanas
resultado_total = promedio_temperatura(temperaturas, ciudades)
print("\nPromedio de temperatura por ciudad durante todas las semanas:")
for ciudad, promedio in resultado_total.items():
    print(f'{ciudad}: {promedio:.2f}°C')
