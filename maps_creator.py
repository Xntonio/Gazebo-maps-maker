# Abrimos el archivo de texto y leemos su contenido
filename = "map.txt"
with open(filename) as file:
    content = file.readlines()

# Calculamos el número de líneas y el ancho del texto
num_lines = len(content)
width = len(content[0].strip())

# Creamos un diccionario para almacenar las coordenadas de cada letra
letras = {}

# Procesamos cada línea del archivo en orden inverso para obtener las coordenadas de cada letra
for y, line in enumerate(reversed(content)):
    for x, char in enumerate(line.strip()):
        if char != " ":
            # La posición contiene una letra, la agregamos al diccionario
            if char not in letras:
                letras[char] = []
            # Ajustamos las coordenadas para que (0,0) esté abajo y en el medio
            letras[char].append((((x - width // 2)*-1), y))

# Imprimimos las coordenadas de cada letra
for letra, coordenadas in letras.items():
    print(f"La letra '{letra}' tiene las siguientes coordenadas: {coordenadas}")

coordenadas = letras
filename = 'coordenadas.txt'

# Abrimos el archivo en modo escritura
with open(filename, 'w') as file:
    # Recorremos el diccionario de coordenadas en orden descendente
    for letra in sorted(coordenadas.keys(), reverse=True):
        # Recorremos las coordenadas de la letra y las agregamos al modelo de caja
        for i, (x, y) in enumerate(coordenadas[letra]):
            box_model = f'<include>\n<uri>model://big_box</uri>\n<pose>{y} {x} 0 0 0 0</pose>\n</include>\n'
            # Escribimos el modelo de caja en el archivo de texto
            file.write(box_model)
