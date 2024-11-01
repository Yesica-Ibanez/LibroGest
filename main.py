from usuarios import crear_usuario, leer_usuarios, actualizar_usuario, eliminar_usuario
from libros import crear_libro, leer_libros, actualizar_libro, eliminar_libro
from autores import crear_autor, leer_autores, actualizar_autor, eliminar_autor
from prestamos import crear_prestamo, leer_prestamos, actualizar_prestamo, eliminar_prestamo
from multas import crear_multa, leer_multas, actualizar_multa, eliminar_multa
from accesos import crear_acceso, leer_accesos, actualizar_acceso, eliminar_acceso

def mostrar_menu():
    print("\n--- Gestor de Biblioteca ---")
    print("1. Gestionar Usuarios")
    print("2. Gestionar Libros")
    print("3. Gestionar Autores")
    print("4. Gestionar Préstamos")
    print("5. Gestionar Multas")
    print("6. Gestionar Accesos")
    print("0. Salir")

# Menús para cada entidad
def menu_usuarios():
    print("\n--- Menú de Usuarios ---")
    print("1. Crear Usuario")
    print("2. Leer Usuarios")
    print("3. Actualizar Usuario")
    print("4. Eliminar Usuario")
    print("0. Volver al Menú Principal")
    return input("Selecciona una opción: ")

def menu_libros():
    print("\n--- Menú de Libros ---")
    print("1. Crear Libro")
    print("2. Leer Libros")
    print("3. Actualizar Libro")
    print("4. Eliminar Libro")
    print("0. Volver al Menú Principal")
    return input("Selecciona una opción: ")

def menu_autores():
    print("\n--- Menú de Autores ---")
    print("1. Crear Autor")
    print("2. Leer Autores")
    print("3. Actualizar Autor")
    print("4. Eliminar Autor")
    print("0. Volver al Menú Principal")
    return input("Selecciona una opción: ")

def menu_prestamos():
    print("\n--- Menú de Préstamos ---")
    print("1. Crear Préstamo")
    print("2. Leer Préstamos")
    print("3. Actualizar Préstamo")
    print("4. Eliminar Préstamo")
    print("0. Volver al Menú Principal")
    return input("Selecciona una opción: ")

def menu_multas():
    print("\n--- Menú de Multas ---")
    print("1. Crear Multa")
    print("2. Leer Multas")
    print("3. Actualizar Multa")
    print("4. Eliminar Multa")
    print("0. Volver al Menú Principal")
    return input("Selecciona una opción: ")

def menu_accesos():
    print("\n--- Menú de Accesos ---")
    print("1. Crear Acceso")
    print("2. Leer Accesos")
    print("3. Actualizar Acceso")
    print("4. Eliminar Acceso")
    print("0. Volver al Menú Principal")
    return input("Selecciona una opción: ")

# Funciones para gestionar cada entidad
def ejecutar_gestion_usuarios():
    while True:
        opcion = menu_usuarios()
        if opcion == "1":
            username = input("Ingrese el nombre de usuario: ")
            password = input("Ingrese la contraseña: ")
            email = input("Ingrese el correo electrónico: ")
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            crear_usuario(username, password, email, nombre, apellido)
        elif opcion == "2":
            leer_usuarios()
        elif opcion == "3":
            id_usuario = int(input("Ingrese el ID del usuario a actualizar: "))
            nombre = input("Ingrese el nuevo nombre (dejar en blanco para no modificar): ")
            apellido = input("Ingrese el nuevo apellido (dejar en blanco para no modificar): ")
            estado = input("Ingrese el nuevo estado de membresía (dejar en blanco para no modificar): ")
            actualizar_usuario(id_usuario, nombre or None, apellido or None, estado or None)
        elif opcion == "4":
            id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
            eliminar_usuario(id_usuario)
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

# (Repetir `ejecutar_gestion_` para Libros, Autores, Préstamos, Multas y Accesos)

def ejecutar_gestion_libros():
    while True:
        opcion = menu_libros()
        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            id_autor = int(input("Ingrese el ID del autor: "))
            genero = input("Ingrese el género del libro: ")
            anio_publicacion = int(input("Ingrese el año de publicación: "))
            editorial = input("Ingrese la editorial: ")
            crear_libro(titulo, id_autor, genero, anio_publicacion, editorial)
        elif opcion == "2":
            leer_libros()
        elif opcion == "3":
            id_libro = int(input("Ingrese el ID del libro a actualizar: "))
            titulo = input("Ingrese el nuevo título (dejar en blanco para no modificar): ")
            genero = input("Ingrese el nuevo género (dejar en blanco para no modificar): ")
            anio_publicacion = input("Ingrese el nuevo año de publicación (dejar en blanco para no modificar): ")
            editorial = input("Ingrese la nueva editorial (dejar en blanco para no modificar): ")
            actualizar_libro(id_libro, titulo or None, id_autor or None, genero or None, anio_publicacion or None, editorial or None)
        elif opcion == "4":
            id_libro = int(input("Ingrese el ID del libro a eliminar: "))
            eliminar_libro(id_libro)
        elif opcion == "0":
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

# Repetir para `Autores`, `Prestamos`, `Multas`, y `Accesos` de manera similar

# Código Principal
if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            ejecutar_gestion_usuarios()
        elif opcion == "2":
            ejecutar_gestion_libros()
        elif opcion == "3":
            # ejecutar_gestion_autores()
            pass
        elif opcion == "4":
            # ejecutar_gestion_prestamos()
            pass
        elif opcion == "5":
            # ejecutar_gestion_multas()
            pass
        elif opcion == "6":
            # ejecutar_gestion_accesos()
            pass
        elif opcion == "0":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
