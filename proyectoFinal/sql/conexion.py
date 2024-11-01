import mysql.connector
from mysql.connector import Error

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='',  
            password='',  
            database='Biblioteca'
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None

def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
