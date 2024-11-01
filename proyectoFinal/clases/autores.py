from sql.conexion import crear_conexion, cerrar_conexion
from mysql.connector import Error


def crear_autor(nombre, bibliografia=None):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
                INSERT INTO Autores (nombre, bibliografia)
                VALUES (%s, %s)
            """
            valores = (nombre, bibliografia)
            cursor.execute(consulta, valores)
            conexion.commit()
            print("Autor creado exitosamente.")
        except Error as e:
            print(f"Error al crear autor: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

#  leer todos los autores
def leer_autores():
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "SELECT * FROM Autores"
            cursor.execute(consulta)
            autores = cursor.fetchall()
            for autor in autores:
                print(autor)
        except Error as e:
            print(f"Error al leer autores: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

#  actualizar un autor
def actualizar_autor(id_autor, nombre=None, bibliografia=None):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "UPDATE Autores SET "
            valores = []
            if nombre:
                consulta += "nombre = %s, "
                valores.append(nombre)
            if bibliografia:
                consulta += "bibliografia = %s, "
                valores.append(bibliografia)
            consulta = consulta.rstrip(", ")  # Quitamos la coma final
            consulta += " WHERE id_autor = %s"
            valores.append(id_autor)
            cursor.execute(consulta, tuple(valores))
            conexion.commit()
            print("Autor actualizado exitosamente.")
        except Error as e:
            print(f"Error al actualizar autor: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

#  eliminar un autor
def eliminar_autor(id_autor):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "DELETE FROM Autores WHERE id_autor = %s"
            cursor.execute(consulta, (id_autor,))
            conexion.commit()
            print("Autor eliminado exitosamente.")
        except Error as e:
            print(f"Error al eliminar autor: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)
