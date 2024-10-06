-- Crear la base de datos
CREATE DATABASE Biblioteca;

-- Usar la base de datos
USE Biblioteca;

-- Crear tabla Usuarios
CREATE TABLE Usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    email VARCHAR(100) UNIQUE,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    estado_membresia VARCHAR(20) DEFAULT 'ACTIVA'
);

-- Crear tabla Accesos
CREATE TABLE Accesos (
    id_acceso INT PRIMARY KEY AUTO_INCREMENT,
    fechaIngreso DATETIME,
    fechaSalida DATETIME,
    usuarioLogueado INT,
    FOREIGN KEY (usuarioLogueado) REFERENCES Usuarios(id_usuario)
);

-- Crear tabla Autores
CREATE TABLE Autores (
    id_autor INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    bibliografia TEXT
);

-- Crear tabla Libros
CREATE TABLE Libros (
    id_libro INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(255),
    id_autor INT,
    genero VARCHAR(100),
    anio_publicacion YEAR,
    editorial VARCHAR(100),
    FOREIGN KEY (id_autor) REFERENCES Autores(id_autor)
);

-- Crear tabla Prestamos
CREATE TABLE Prestamos (
    id_prestamo INT PRIMARY KEY AUTO_INCREMENT,
    id_libro INT,
    id_usuario INT,
    fecha_prestamo DATE,
    fecha_devolucion DATE,
    estado VARCHAR(20) DEFAULT 'VIGENTE',
    FOREIGN KEY (id_libro) REFERENCES Libros(id_libro),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Crear tabla Multas
CREATE TABLE Multas (
    id_multa INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    fecha_multa DATE,
    motivo VARCHAR(255),
    estado VARCHAR(20),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

