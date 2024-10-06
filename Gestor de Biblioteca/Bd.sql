CREATE DATABASE IF NOT EXISTS Biblioteca;

USE Biblioteca;

--  tabla Usuarios
CREATE TABLE IF NOT EXISTS Usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    estado_membresia VARCHAR(20) DEFAULT 'ACTIVA'
);

--  tabla Accesos para registrar los ingresos al sistema
CREATE TABLE IF NOT EXISTS Accesos (
    id_acceso INT PRIMARY KEY AUTO_INCREMENT,
    fechaIngreso DATETIME NOT NULL,
    fechaSalida DATETIME,
    usuarioLogueado INT NOT NULL,
    FOREIGN KEY (usuarioLogueado) REFERENCES Usuarios(id_usuario) ON DELETE CASCADE
);

--  tabla Autores para almacenar información de autores
CREATE TABLE IF NOT EXISTS Autores (
    id_autor INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    bibliografia TEXT
);

--  tabla Obras para asociar obras publicadas por cada autor
CREATE TABLE IF NOT EXISTS Obras (
    id_obra INT PRIMARY KEY AUTO_INCREMENT,
    id_autor INT NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_autor) REFERENCES Autores(id_autor) ON DELETE CASCADE
);

--  tabla Libros para registrar los libros disponibles en la biblioteca
CREATE TABLE IF NOT EXISTS Libros (
    id_libro INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(255) NOT NULL,
    id_autor INT, -- Permitir NULL para que ON DELETE SET NULL funcione
    genero VARCHAR(100) NOT NULL,
    anio_publicacion YEAR NOT NULL,
    editorial VARCHAR(100),
    FOREIGN KEY (id_autor) REFERENCES Autores(id_autor) ON DELETE SET NULL
);

--  tabla Prestamos para gestionar los préstamos de libros
CREATE TABLE IF NOT EXISTS Prestamos (
    id_prestamo INT PRIMARY KEY AUTO_INCREMENT,
    id_libro INT NOT NULL,
    id_usuario INT NOT NULL,
    fecha_prestamo DATE NOT NULL,
    fecha_devolucion DATE NOT NULL,
    estado VARCHAR(20) DEFAULT 'VIGENTE',
    FOREIGN KEY (id_libro) REFERENCES Libros(id_libro) ON DELETE CASCADE,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario) ON DELETE CASCADE
);

--  tabla Multas para gestionar las multas de los usuarios
CREATE TABLE IF NOT EXISTS Multas (
    id_multa INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    fecha_multa DATE NOT NULL,
    motivo VARCHAR(255) NOT NULL,
    estado VARCHAR(20) DEFAULT 'PENDIENTE',
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario) ON DELETE CASCADE
);

-- Verificar las tablas creadas
SHOW TABLES;
