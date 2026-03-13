CREATE DATABASE "hoteleriaBD";

\c "hoteleriaBD"

CREATE TABLE Hotel (
    id_hotel SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    habitacion_ocupada INT DEFAULT 0,
    habitacion_disponible INT DEFAULT 0
);

CREATE TABLE Tipo_habitacion (
    id_tipo_habitacion SERIAL PRIMARY KEY,
    tipo_habitacion VARCHAR(100) NOT NULL
);

CREATE TABLE Estado (
    id_tipo_estado SERIAL PRIMARY KEY,
    estado VARCHAR(50) NOT NULL
);

CREATE TABLE Administrador (
    id_admin SERIAL PRIMARY KEY,
    nombre_admin VARCHAR(150) NOT NULL,
    id_hotel INT NOT NULL REFERENCES Hotel(id_hotel) ON DELETE CASCADE
);

CREATE TABLE Recepcionista (
    id_recepcionista SERIAL PRIMARY KEY,
    nombre_recepcionista VARCHAR(150) NOT NULL,
    id_hotel INT NOT NULL REFERENCES Hotel(id_hotel) ON DELETE CASCADE
);

CREATE TABLE Cliente (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    numero_documento VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(150),
    id_hotel INT NOT NULL REFERENCES Hotel(id_hotel) ON DELETE CASCADE
);

CREATE TABLE Habitual (
    id_tipo_cliente INT PRIMARY KEY REFERENCES Cliente(id_cliente) ON DELETE CASCADE,
    descuento DECIMAL(5,2)
);

CREATE TABLE Esporadico (
    id_tipo_cliente INT PRIMARY KEY REFERENCES Cliente(id_cliente) ON DELETE CASCADE
);

CREATE TABLE Habitacion (
    numero_habitacion VARCHAR(50) PRIMARY KEY,
    tipo_habitacion VARCHAR(100),
    id_tipo_habitacion INT REFERENCES Tipo_habitacion(id_tipo_habitacion),
    foto TEXT,
    precio DECIMAL(10,2) NOT NULL,
    id_estado INT REFERENCES Estado(id_tipo_estado),
    id_hotel INT NOT NULL REFERENCES Hotel(id_hotel) ON DELETE CASCADE,
    id_recepcionista INT REFERENCES Recepcionista(id_recepcionista) ON DELETE SET NULL,
    id_admin INT REFERENCES Administrador(id_admin) ON DELETE SET NULL
);

CREATE TABLE Reserva (
    id_reserva SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL REFERENCES Cliente(id_cliente),
    numero_habitacion VARCHAR(50) NOT NULL REFERENCES Habitacion(numero_habitacion),
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    dias_noches INT NOT NULL,
    nombre_cliente VARCHAR(150),
    precio_total DECIMAL(10,2) NOT NULL
);