import random, pprint
#Ejemplo de canción: cancion = {"nombre":"Sweet Child O' Mine","autor":"Guns N' roses","genero":"rock"}

# Parte 1: Carga y Manipulación de Listas de Música
# 1.1. Cargar Lista de Música desde Archivo: (1 punto)
# Escribe una función llamada cargar_lista que tome el nombre de un archivo de texto como argumento y devuelva un diccionario de canciones. Cada clave del diccionario debe ser el título de una canción y cada valor debe ser el nombre del artista.

def cargar_lista(nombreFichero):
    lista_canciones=[]
    with open(nombreFichero,"r") as fichero:
        for linea in fichero:
            valores = linea.strip().split(" - ")
            if len(valores)==3:
                nombre, artista, genero = valores
                cancion = {'nombre': nombre, 'artista': artista, 'genero': genero}
                lista_canciones.append(cancion)
                
            else:
                print("Estructura del fichero incorrecta")
                break
    return lista_canciones

# 1.2. Agregar Canción a Lista de Música: (1 punto)
# Escribe una función llamada agregar_cancion que tome un diccionario de canciones, el nombre de una nueva canción y el nombre del artista como argumentos, y agregue la nueva canción al diccionario.

def agregar_cancion(lista_canciones, nombre, artista, genero):
    encontrado = False
    for cancion in lista_canciones:
        if cancion["nombre"] == nombre:
            encontrado = True
            break

    if encontrado:
        print(f"La canción {nombre} está ya en la lista.")
    else:
        nueva_cancion = {'nombre':nombre, 'artista':artista, 'genero':genero}
        lista_canciones.append(nueva_cancion)
        print(f"La canción {nombre} se ha añadido a la lista.")

    return lista_canciones

# 1.3. Eliminar Canción de Lista de Música: (1 punto)
# Escribe una función llamada eliminar_cancion que tome un diccionario de canciones y el título de una canción como argumentos, y elimine la canción del diccionario si está presente.
def eliminar_cancion(lista_canciones, nombre):
    encontrado = False
    for i, cancion in enumerate(lista_canciones):
        if cancion["nombre"] == nombre:
            encontrado = True
            break

    if not encontrado:
        print(f"La canción {nombre} no está en la lista.")
    else:
        del lista_canciones[i]
        print(f"La canción {nombre} se ha eliminado de la lista.")

    return lista_canciones


# Parte 2: Análisis de Listas de Música
# 2.1. Contar Canciones en una Lista: (1 punto)
# Escribe una función llamada contar_canciones que tome un diccionario de canciones como argumento y devuelva el número total de canciones en el diccionario.

def contar_canciones(diccionario):
    return len(diccionario)


# 2.2. Buscar Canciones por Artista: (2 puntos)
# Escribe una función llamada buscar_por_artista que tome un diccionario de canciones y el nombre de un artista como argumentos, y devuelva una lista de todas las canciones de ese artista.


# 2.3. Ordenar Lista de Música Alfabéticamente: (1 punto)
# Escribe una función llamada ordenar_alfabeticamente que tome un diccionario de canciones como argumento y devuelva una lista de tuplas ordenadas alfabéticamente por título de canción.

# Parte 3: Creación de Listas de Reproducción
# 3.1. Crear Lista de Reproducción Aleatoria: (2 puntos)
# Escribe una función llamada crear_lista_aleatoria que tome un diccionario de canciones y un número n como argumentos, y devuelva una lista aleatoria de n canciones del diccionario de canciones original.

def crear_lista_aleatoria(diccionario , n):
    n = min(n , len(diccionario))
    lista = random.sample(diccionario.items() , n)
    return lista


# 3.2. Guardar Lista de Reproducción en Archivo: (1 punto)
# Escribe una función llamada guardar_lista que tome un diccionario de canciones y el nombre de un archivo como argumentos, y guarde todas las canciones del diccionario en el archivo de texto, una por línea, en el formato "título de la canción - artista".
def guardar_lista(lista_canciones, nombreArchivo):
    
    with open(nombreArchivo, "w") as fichero:
        for cancion in lista_canciones:
            fichero.write(f"{cancion['nombre']} - {cancion['artista']} - {cancion['genero']}\n")

biblioteca_musical=cargar_lista("biblioteca.txt")

biblioteca_musical=agregar_cancion(biblioteca_musical,'Mi canción','JI','Rock')
#biblioteca_musical=eliminar_cancion(biblioteca_musical,'Mi canción')
#pprint.pprint(biblioteca_musical, width=40)
# eliminar_cancion(listaCanciones, "Yesterday")
guardar_lista(biblioteca_musical, "biblioteca_modificada.txt")

# print(crear_lista_aleatoria(listaCanciones , 3))