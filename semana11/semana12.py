
ciudades = ['Ciudad_Loja', 'Ciudad_Machala', 'Ciudad_Quito']
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4  # Supongamos 4 semanas de datos
# Generar datos de temperaturas aleatorias (en °C) para cada ciudad, día y semana
 np.random.seed(42)  # Para reproducibilidad
temperaturas = np.random.uniform(15, 35, (len(ciudades), len(dias), semanas))

# Inicializar diccionario para almacenar los promedios
promedios = {ciudad: [] for ciudad in ciudades}

# Calcular el promedio de temperaturas por semana para cada ciudad utilizando bucles anidados
for i, ciudad in enumerate(ciudades):
    for semana in range(semanas):
        suma_temperaturas = 0
        for dia in range(len(dias)):
            suma_temperaturas += temperaturas[i][dia][semana]
        promedio_semanal = suma_temperaturas / len(dias)
        promedios[ciudad].append(promedio_semanal)

# Mostrar los promedios de temperatura para cada ciudad y semana
for ciudad, promedios_semanales in promedios.items():
    print(f"Promedios de temperaturas para {ciudad}:")
    for semana, promedio in enumerate(promedios_semanales, 1):
        print(f"  Semana {semana}: {promedio:.2f}°C")
