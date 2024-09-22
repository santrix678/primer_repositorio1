# Definición de la función calcular_descuento con las llamadas completas
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el descuento aplicando el porcentaje al monto total
    descuento = monto_total * (porcentaje_descuento / 100)
    # Devuelve el monto del descuento calculado
    return descuento

# Llamada a la función 1: usando el valor por defecto del porcentaje de descuento (10%)
monto_1 = 50  # Ejemplo de monto total de la compra
descuento_1 = calcular_descuento(monto_1)
monto_final_1 = monto_1 - descuento_1

# Llamada a la función 2: especificando tanto el monto total como el porcentaje de descuento
monto_2 = 100  # Otro ejemplo de monto total de la compra
porcentaje_descuento_2 = 15  # Descuento del 15%
descuento_2 = calcular_descuento(monto_2, porcentaje_descuento_2)
monto_final_2 = monto_2 - descuento_2

# Resultados de las dos llamadas
(monto_1, descuento_1, monto_final_1), (monto_2, descuento_2, monto_final_2)
# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el descuento aplicando el porcentaje al monto total
    descuento = monto_total * (porcentaje_descuento / 100)
    # Devuelve el monto del descuento calculado
    return descuento

# Llamada a la función 1: usando el valor por defecto del porcentaje de descuento (10%)
monto_1 = 50  # Ejemplo de monto total de la compra
descuento_1 = calcular_descuento(monto_1)
monto_final_1 = monto_1 - descuento_1
print(f"Compra 1 - Monto: ${monto_1}, Descuento: ${descuento_1}, Monto final: ${monto_final_1}")

# Llamada a la función 2: especificando tanto el monto total como el porcentaje de descuento
monto_2 = 100  # Otro ejemplo de monto total de la compra
porcentaje_descuento_2 = 15  # Descuento del 15%
descuento_2 = calcular_descuento(monto_2, porcentaje_descuento_2)
monto_final_2 = monto_2 - descuento_2
print(f"Compra 2 - Monto: ${monto_2}, Descuento: ${descuento_2}, Monto final: ${monto_final_2}")


