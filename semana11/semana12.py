# Definir las ciudades y los días de la semana
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Crear una matriz tridimensional (ciudades x días x semanas)
# Supongamos que tenemos datos para 2 semanas, y cada día tiene una temperatura aleatoria
import random

# Generar datos de temperaturas aleatorios para simplificar el ejemplo
temperaturas = [[[random.uniform(10.0, 30.0) for dia in range(len(dias_semana))] for semana in range(2)] for ciudad in ciudades]

# Imprimir los datos de temperaturas
print("Datos de temperaturas (en °C):")
for idx_ciudad, ciudad in enumerate(ciudades):
    for idx_semana, semana in enumerate(temperaturas[idx_ciudad]):
        print(f"{ciudad}, Semana {idx_semana + 1}: {semana}")

# Calcular el promedio de temperaturas por semana para cada ciudad
print("\nPromedios de temperaturas por semana:")
for idx_ciudad, ciudad in enumerate(ciudades):
    for idx_semana, semana in enumerate(temperaturas[idx_ciudad]):
        promedio_semana = sum(semana) / len(semana)
        print(f"El promedio de temperatura en {ciudad} para la semana {idx_semana + 1} es: {promedio_semana:.2f}°C")

