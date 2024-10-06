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
            password='colocar contraseña'  
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
        return usuario
    else:
        with open('logs.txt', 'a') as file:
            file.write(f"Fallo de ingreso: {username}, {password}, {datetime.datetime.now()}\n")
        print("Credenciales incorrectas")
        return None

def guardar_acceso_binario(acceso):
    with open('accesos.ispc', 'ab') as file:
        pickle.dump(acceso, file)

# funciones CRUD, actualizar y eliminar usuario, y otras funcionalidades 

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
                if usuario:
                    print("Acceso a opciones de usuario...")
            elif opcion == '3':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida")
    else:
        print("No se pudo establecer la conexión con la base de datos.")


