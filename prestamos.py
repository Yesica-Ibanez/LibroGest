from sql.conexion import crear_conexion, cerrar_conexion
from mysql.connector import Error

# registrar un préstamo
def crear_prestamo(id_libro, id_usuario, fecha_prestamo, fecha_devolucion, estado="VIGENTE"):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
                INSERT INTO Prestamos (id_libro, id_usuario, fecha_prestamo, fecha_devolucion, estado)
                VALUES (%s, %s, %s, %s, %s)
            """
            valores = (id_libro, id_usuario, fecha_prestamo, fecha_devolucion, estado)
            cursor.execute(consulta, valores)
            conexion.commit()
            print("Préstamo creado exitosamente.")
        except Error as e:
            print(f"Error al crear préstamo: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

#  leer todos los préstamos
def leer_prestamos():
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "SELECT * FROM Prestamos"
            cursor.execute(consulta)
            prestamos = cursor.fetchall()
            for prestamo in prestamos:
                print(prestamo)
        except Error as e:
            print(f"Error al leer préstamos: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

#  actualizar un préstamo
def actualizar_prestamo(id_prestamo, fecha_devolucion=None, estado=None):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "UPDATE Prestamos SET "
            valores = []
            if fecha_devolucion:
                consulta += "fecha_devolucion = %s, "
                valores.append(fecha_devolucion)
            if estado:
                consulta += "estado = %s, "
                valores.append(estado)
            consulta = consulta.rstrip(", ")  # Quitamos la coma final
            consulta += " WHERE id_prestamo = %s"
            valores.append(id_prestamo)
            cursor.execute(consulta, tuple(valores))
            conexion.commit()
            print("Préstamo actualizado exitosamente.")
        except Error as e:
            print(f"Error al actualizar préstamo: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

#  eliminar un préstamo
def eliminar_prestamo(id_prestamo):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "DELETE FROM Prestamos WHERE id_prestamo = %s"
            cursor.execute(consulta, (id_prestamo,))
            conexion.commit()
            print("Préstamo eliminado exitosamente.")
        except Error as e:
            print(f"Error al eliminar préstamo: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)
