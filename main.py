# main.py
import funciones_biblioteca

def menu():
    print("\n************************* \n")
    print("***** MENU PRINCIPAL *****")
    print("Bienvenido a la biblioteca")
    print("1. Agregar un nuevo libro")
    print("2. Buscar un libro por título")
    print("3. Mostrar todos los libros disponibles")
    print("4. Salir del programa")

    opcion = input("**Selecciona una opcion: ")
    print("\n************************* \n")

    if opcion == "1":
        funciones_biblioteca.agregar_libro()
    elif opcion == "2":
        funciones_biblioteca.buscar_libro()
    elif opcion == "3":
        funciones_biblioteca.mostrar_libros()
    elif opcion == "4":
        print("Hasta luego!")
        return
    else:
        print("Opción inválida. Por favor, inténtalo de nuevo.")

    menu()

if __name__ == "__main__":
    menu()