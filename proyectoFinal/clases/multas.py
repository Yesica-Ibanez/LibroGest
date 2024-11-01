from sql.conexion import crear_conexion, cerrar_conexion
from mysql.connector import Error

#  crear una multa
def crear_multa(id_usuario, fecha_multa, motivo, estado="PENDIENTE"):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
                INSERT INTO Multas (id_usuario, fecha_multa, motivo, estado)
                VALUES (%s, %s, %s, %s)
            """
            valores = (id_usuario, fecha_multa, motivo, estado)
            cursor.execute(consulta, valores)
            conexion.commit()
            print("Multa creada exitosamente.")
        except Error as e:
            print(f"Error al crear multa: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

#  leer todas las multas
def leer_multas():
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "SELECT * FROM Multas"
            cursor.execute(consulta)
            multas = cursor.fetchall()
            for multa in multas:
                print(multa)
        except Error as e:
            print(f"Error al leer multas: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

#  actualizar una multa
def actualizar_multa(id_multa, estado=None, motivo=None):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "UPDATE Multas SET "
            valores = []
            if estado:
                consulta += "estado = %s, "
                valores.append(estado)
            if motivo:
                consulta += "motivo = %s, "
                valores.append(motivo)
            consulta = consulta.rstrip(", ")  # Quitamos la coma final
            consulta += " WHERE id_multa = %s"
            valores.append(id_multa)
            cursor.execute(consulta, tuple(valores))
            conexion.commit()
            print("Multa actualizada exitosamente.")
        except Error as e:
            print(f"Error al actualizar multa: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

#  eliminar una multa
def eliminar_multa(id_multa):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "DELETE FROM Multas WHERE id_multa = %s"
            cursor.execute(consulta, (id_multa,))
            conexion.commit()
            print("Multa eliminada exitosamente.")
        except Error as e:
            print(f"Error al eliminar multa: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)
