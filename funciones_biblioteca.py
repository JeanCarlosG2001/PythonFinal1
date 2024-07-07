# funciones_biblioteca.py

import os

def agregar_libro():
    #Imputs
    titulo = input("Ingresa el título del libro: ")
    autor = input("Ingresa el autor del libro: ")
    año = input("Ingresa el año de publicación del libro: ")

    # Almacenar datos
    libro = {
        "titulo": titulo,
        "autor": autor,
        "año": año
    }

    # Agregar el nuevo libro a una lista de libros
    libros = []
    libros.append(libro)

    print("Libro agregado exitosamente.")

    # Crear una carpeta llamada "libros"
    if not os.path.exists("libros"):
        os.makedirs("libros")

    # Crear un archivo .txt
    with open(f"libros/{titulo}.txt", "w") as file:
        file.write(f"Titulo: {titulo}\nAutor: {autor}\nAno: {año}")

    print(f"Los datos del libro se han guardado en libros/{titulo}.txt")

    pass

def buscar_libro():
    #Input
    titulo = input("Ingresa el título del libro que estás buscando: ")

    #Error en caso de que no exista la carpeta "libros"
    libros_dir = "libros"
    if not os.path.exists(libros_dir):
        print(f"No se encontró la carpeta {libros_dir}.")
        return
    
    libros = os.listdir(libros_dir)
    libros_txt = [libro for libro in libros if libro.endswith(".txt")]

    if f"{titulo}.txt" in libros_txt:
        print(f"El libro {titulo} se encontró en {libros_dir}.")
        print("quieres leerlo? 1. si 2. no: ")
        respuesta = input()
        if respuesta == "1":
            with open(f"{libros_dir}/{titulo}.txt", "r") as file:
                print(file.read())

        elif respuesta == "2":
            print("Regresando al menu...")
        else:
            print("Opción inválida. Por favor, inténtalo de nuevo.")
    else:
        print(f"No se encontró el libro {titulo} en {libros_dir}.")
    pass


def mostrar_libros():
    libros_dir = "libros"
    if not os.path.exists(libros_dir):
        print(f"No se encontró la carpeta {libros_dir}.")
        return
    libros = os.listdir(libros_dir)
    libros_txt = [os.path.splitext(libro)[0] for libro in libros if libro.endswith(".txt")]
    print(f"Los libros disponibles son: {', '.join(libros_txt)}")
    pass