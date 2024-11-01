from sql.conexion import crear_conexion, cerrar_conexion
from mysql.connector import Error

#  crear un libro
def crear_libro(titulo, id_autor=None, genero=None, anio_publicacion=None, editorial=None):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = """
                INSERT INTO Libros (titulo, id_autor, genero, anio_publicacion, editorial)
                VALUES (%s, %s, %s, %s, %s)
            """
            valores = (titulo, id_autor, genero, anio_publicacion, editorial)
            cursor.execute(consulta, valores)
            conexion.commit()
            print("Libro creado exitosamente.")
        except Error as e:
            print(f"Error al crear libro: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

#  leer todos los libros
def leer_libros():
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "SELECT * FROM Libros"
            cursor.execute(consulta)
            libros = cursor.fetchall()
            for libro in libros:
                print(libro)
        except Error as e:
            print(f"Error al leer libros: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

#  actualizar un libro
def actualizar_libro(id_libro, titulo=None, id_autor=None, genero=None, anio_publicacion=None, editorial=None):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "UPDATE Libros SET "
            valores = []
            if titulo:
                consulta += "titulo = %s, "
                valores.append(titulo)
            if id_autor:
                consulta += "id_autor = %s, "
                valores.append(id_autor)
            if genero:
                consulta += "genero = %s, "
                valores.append(genero)
            if anio_publicacion:
                consulta += "anio_publicacion = %s, "
                valores.append(anio_publicacion)
            if editorial:
                consulta += "editorial = %s, "
                valores.append(editorial)
            consulta = consulta.rstrip(", ")  # Quitamos la coma final
            consulta += " WHERE id_libro = %s"
            valores.append(id_libro)
            cursor.execute(consulta, tuple(valores))
            conexion.commit()
            print("Libro actualizado exitosamente.")
        except Error as e:
            print(f"Error al actualizar libro: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)

# eliminar un libro
def eliminar_libro(id_libro):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "DELETE FROM Libros WHERE id_libro = %s"
            cursor.execute(consulta, (id_libro,))
            conexion.commit()
            print("Libro eliminado exitosamente.")
        except Error as e:
            print(f"Error al eliminar libro: {e}")
        finally:
            cursor.close()
            cerrar_conexion(conexion)
