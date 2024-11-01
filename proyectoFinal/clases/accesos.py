from sql.conexion import crear_conexion, cerrar_conexion
from mysql.connector import Error

#  registrar un acceso
def crear_acceso(fechaIngreso, usuarioLogueado, fechaSalida=None):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
                INSERT INTO Accesos (fechaIngreso, fechaSalida, usuarioLogueado)
                VALUES (%s, %s, %s)
            """
            valores = (fechaIngreso, fechaSalida, usuarioLogueado)
            cursor.execute(consulta, valores)
            conexion.commit()
            print("Acceso registrado exitosamente.")
        except Error as e:
            print(f"Error al registrar acceso: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

#  leer todos los accesos
def leer_accesos():
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "SELECT * FROM Accesos"
            cursor.execute(consulta)
            accesos = cursor.fetchall()
            for acceso in accesos:
                print(acceso)
        except Error as e:
            print(f"Error al leer accesos: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

#  actualizar la salida de un acceso
def actualizar_acceso(id_acceso, fechaSalida):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "UPDATE Accesos SET fechaSalida = %s WHERE id_acceso = %s"
            valores = (fechaSalida, id_acceso)
            cursor.execute(consulta, valores)
            conexion.commit()
            print("Acceso actualizado exitosamente.")
        except Error as e:
            print(f"Error al actualizar acceso: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

#  eliminar un acceso
def eliminar_acceso(id_acceso):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "DELETE FROM Accesos WHERE id_acceso = %s"
            cursor.execute(consulta, (id_acceso,))
            conexion.commit()
            print("Acceso eliminado exitosamente.")
        except Error as e:
            print(f"Error al eliminar acceso: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)
