import mysql.connector
from mysql.connector import Error
import pickle
import datetime

class Usuario:
    def __init__(self, username, password, email, nombre, apellido):
        self.username = username
        self.password = password
        self.email = email
        self.nombre = nombre
        self.apellido = apellido

class Acceso:
    def __init__(self, usuario):
        self.fechaIngreso = datetime.datetime.now()
        self.fechaSalida = None
        self.usuarioLogueado = usuario

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='Biblioteca',
            user='root',  
            password='escribir contraseña'  
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
        return connection
    except Error as e:
        print(f"Error al conectar: {e}")
        return None

def registrar_usuario(connection):
    username = input("Ingrese username: ")
    password = input("Ingrese password: ")
    email = input("Ingrese email: ")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")

    usuario = Usuario(username, password, email, nombre, apellido)
    cursor = connection.cursor()
    query = "INSERT INTO Usuarios (username, password, email, nombre, apellido) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (usuario.username, usuario.password, usuario.email, usuario.nombre, usuario.apellido))
    connection.commit()
    guardar_usuario_binario(usuario)
    print("Usuario registrado exitosamente")

def guardar_usuario_binario(usuario):
    with open('usuarios.ispc', 'ab') as file:
        pickle.dump(usuario, file)

def iniciar_sesion(connection):
    username = input("Ingrese username: ")
    password = input("Ingrese password: ")

    cursor = connection.cursor()
    query = "SELECT * FROM Usuarios WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    usuario = cursor.fetchone()

    if usuario:
        print("Ingreso exitoso")
        acceso = Acceso(usuario[0])
        guardar_acceso_binario(acceso)
        menu_usuario(connection, usuario)
    else:
        with open('logs.txt', 'a') as file:
            file.write(f"Fallo de ingreso: {username}, {password}, {datetime.datetime.now()}\n")
        print("Credenciales incorrectas")

def guardar_acceso_binario(acceso):
    with open('accesos.ispc', 'ab') as file:
        pickle.dump(acceso, file)

def gestion_autores(connection):
    cursor = connection.cursor()
    nombre = input("Ingrese el nombre del autor: ")
    bibliografia = input("Ingrese la bibliografía del autor: ")

    query = "INSERT INTO Autores (nombre, bibliografia) VALUES (%s, %s)"
    cursor.execute(query, (nombre, bibliografia))
    connection.commit()
    print("Autor registrado exitosamente")

    # Añadir obras del autor
    while True:
        agregar_obra = input("¿Desea agregar una obra del autor? (s/n): ")
        if agregar_obra.lower() == 's':
            titulo_obra = input("Ingrese el título de la obra: ")
            query_obra = "INSERT INTO Obras (id_autor, titulo) VALUES (LAST_INSERT_ID(), %s)"
            cursor.execute(query_obra, (titulo_obra,))
            connection.commit()
            print("Obra registrada exitosamente")
        else:
            break

def registrar_libro(connection):
    cursor = connection.cursor()
    titulo = input("Ingrese el título del libro: ")
    id_autor = input("Ingrese el ID del autor: ")
    genero = input("Ingrese el género del libro: ")
    anio_publicacion = input("Ingrese el año de publicación (YYYY): ")
    editorial = input("Ingrese la editorial: ")

    query = "INSERT INTO Libros (titulo, id_autor, genero, anio_publicacion, editorial) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (titulo, id_autor, genero, anio_publicacion, editorial))
    connection.commit()
    print("Libro registrado exitosamente")

def realizar_prestamo(connection, usuario):
    cursor = connection.cursor()
    id_libro = input("Ingrese el ID del libro a prestar: ")
    fecha_prestamo = datetime.datetime.now().strftime('%Y-%m-%d')
    fecha_devolucion = (datetime.datetime.now() + datetime.timedelta(days=14)).strftime('%Y-%m-%d')

    query = "INSERT INTO Prestamos (id_libro, id_usuario, fecha_prestamo, fecha_devolucion, estado) VALUES (%s, %s, %s, %s, 'VIGENTE')"
    cursor.execute(query, (id_libro, usuario[0], fecha_prestamo, fecha_devolucion))
    connection.commit()
    print("Préstamo realizado exitosamente")

def consultar_estado_cuenta(connection, usuario):
    cursor = connection.cursor()

    query_prestamos = """
    SELECT Libros.titulo, Prestamos.fecha_prestamo, Prestamos.fecha_devolucion, Prestamos.estado
    FROM Prestamos
    JOIN Libros ON Prestamos.id_libro = Libros.id_libro
    WHERE Prestamos.id_usuario = %s
    """
    cursor.execute(query_prestamos, (usuario[0],))
    prestamos = cursor.fetchall()

    if prestamos:
        print("\nPréstamos realizados:")
        for prestamo in prestamos:
            print(f"Libro: {prestamo[0]}, Fecha Préstamo: {prestamo[1]}, Fecha Devolución: {prestamo[2]}, Estado: {prestamo[3]}")
    else:
        print("No tienes préstamos registrados.")

    query_multas = "SELECT fecha_multa, motivo, estado FROM Multas WHERE id_usuario = %s"
    cursor.execute(query_multas, (usuario[0],))
    multas = cursor.fetchall()

    if multas:
        print("\nMultas registradas:")
        for multa in multas:
            print(f"Fecha Multa: {multa[0]}, Motivo: {multa[1]}, Estado: {multa[2]}")
    else:
        print("No tienes multas registradas.")

def menu_usuario(connection, usuario):
    while True:
        print("\nMenú del Usuario")
        print("1. Gestión de autores")
        print("2. Registrar libros")
        print("3. Realizar un préstamo")
        print("4. Consultar estado de cuenta")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestion_autores(connection)
        elif opcion == '2':
            registrar_libro(connection)
        elif opcion == '3':
            realizar_prestamo(connection, usuario)
        elif opcion == '4':
            consultar_estado_cuenta(connection, usuario)
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    connection = create_connection()
    if connection:
        while True:
            print("\nMenú Principal")
            print("1. Registrar usuario")
            print("2. Iniciar sesión")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                registrar_usuario(connection)
            elif opcion == '2':
                usuario = iniciar_sesion(connection)
            elif opcion == '3':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida")
    else:
        print("No se pudo establecer la conexión con la base de datos.")

