# Crear el diccionario
informacion_personal = {
    "nombre": "Marcelo Medina",
    "edad": 26,
    "ciudad": "Quito",
    "profesion": "Tecnologias de la informacion"
}

# Modificar la ciudad
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor para la especialidad

# Imprimir el contenido del diccionario
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")