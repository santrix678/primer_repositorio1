# Escritura de un archivo de texto llamado "my_notes.txt" con tres líneas de notas personales

# Crear y escribir en el archivo
with open("my_notes.txt", 'w') as file:
    # Escribir tres líneas de notas personales
    file.write("Mañana preparare el desayuno.\n")
    file.write("Hoy aprendí a manejar archivos moto.\n")
    file.write("Me gusta escuchar musica.\n")

# Lectura del archivo línea por línea
with open("my_notes.txt", 'r') as file:
    # Leer y mostrar cada línea
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # Mostrar cada línea sin saltos de línea adicionales

# El archivo se cierra automáticamente usando la estructura 'with', por lo tanto no es necesario cerrarlo manualmente.






