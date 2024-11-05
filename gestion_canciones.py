import random

# Parte 1: Carga y Manipulación de Listas de Música
# 1.1. Cargar Lista de Música desde Archivo: (1 punto)
# Escribe una función llamada cargar_lista que tome el nombre de un archivo de texto como argumento y devuelva un diccionario de canciones. Cada clave del diccionario debe ser el título de una canción y cada valor debe ser el nombre del artista.

def cargar_lista(nombreFichero):
    diccionario = {}
    with open(nombreFichero,"r") as fichero:
        for linea in fichero:
            cancion,artista = linea.strip().split(" - ")
            diccionario[cancion] = artista
    return diccionario

# 1.2. Agregar Canción a Lista de Música: (1 punto)
# Escribe una función llamada agregar_cancion que tome un diccionario de canciones, el nombre de una nueva canción y el nombre del artista como argumentos, y agregue la nueva canción al diccionario.

def agregar_cancion(diccionario, cancion, artista):
    if cancion in diccionario:
        print("La cancion ya esta introducida.")
    else:
        diccionario[cancion] = artista
        print(f"La cancion {cancion} se ha añadido")
        return diccionario

# 1.3. Eliminar Canción de Lista de Música: (1 punto)
# Escribe una función llamada eliminar_cancion que tome un diccionario de canciones y el título de una canción como argumentos, y elimine la canción del diccionario si está presente.
def eliminar_cancion(diccionario, cancion):
    if cancion in diccionario:
        del diccionario[cancion]
        print(f"La canción {cancion} se ha eliminado")
    else:
        print("La canción no se encuentra en la lista")

# Parte 2: Análisis de Listas de Música
# 2.1. Contar Canciones en una Lista: (1 punto)
# Escribe una función llamada contar_canciones que tome un diccionario de canciones como argumento y devuelva el número total de canciones en el diccionario.

def contar_canciones(diccionario):
    return len(diccionario)


# 2.2. Buscar Canciones por Artista: (2 puntos)
# Escribe una función llamada buscar_por_artista que tome un diccionario de canciones y el nombre de un artista como argumentos, y devuelva una lista de todas las canciones de ese artista.
def buscar_por_artista (diccionario, artista):
    canciones_artista = []
    for cancion in diccionario:
        if diccionario[cancion]==artista:
            canciones_artista.append(cancion)
    return canciones_artista

# 2.3. Ordenar Lista de Música Alfabéticamente: (1 punto)
# Escribe una función llamada ordenar_alfabeticamente que tome un diccionario de canciones como argumento y devuelva una lista de tuplas ordenadas alfabéticamente por título de canción.
def ordenar_alfabeticamente (diccionario):
    return sorted(diccionario)
# Parte 3: Creación de Listas de Reproducción
# 3.1. Crear Lista de Reproducción Aleatoria: (2 puntos)
# Escribe una función llamada crear_lista_aleatoria que tome un diccionario de canciones y un número n como argumentos, y devuelva una lista aleatoria de n canciones del diccionario de canciones original.

def crear_lista_aleatoria(diccionario , n):
    n = min(n , len(diccionario))
    lista = random.sample(diccionario.items() , n)
    return lista


# 3.2. Guardar Lista de Reproducción en Archivo: (1 punto)
# Escribe una función llamada guardar_lista que tome un diccionario de canciones y el nombre de un archivo como argumentos, y guarde todas las canciones del diccionario en el archivo de texto, una por línea, en el formato "título de la canción - artista".
def guardar_lista(diccionario, nombreArchivo):
    
    with open(nombreArchivo, "w") as fichero:
        for cancion, artista in diccionario.items():
            # fichero.write(cancion + " - " + artista)
            fichero.write(f"{cancion} - {artista}\n")

listaCanciones=cargar_lista("playlist.txt")
print(listaCanciones)

# eliminar_cancion(listaCanciones, "Yesterday2")
print(buscar_por_artista(listaCanciones,'The Beatles'))
print(ordenar_alfabeticamente(listaCanciones))

# guardar_lista(listaCanciones, "playlist2.txt")

# print(crear_lista_aleatoria(listaCanciones , 3))