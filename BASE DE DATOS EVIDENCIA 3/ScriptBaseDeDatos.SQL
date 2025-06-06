
CREATE DATABASE IF NOT EXISTS `Usuarios-Roles`;
USE `Usuarios-Roles`;


CREATE TABLE Rol (
    id_rol INTEGER PRIMARY KEY UNIQUE NOT NULL,
    nombre_rol TEXT UNIQUE NOT NULL
);


CREATE TABLE Usuario (
    id_usuario INTEGER PRIMARY KEY UNIQUE NOT NULL,
    nombre TEXT NOT NULL,
    nombre_usuario TEXT UNIQUE NOT NULL,
    contrasena TEXT NOT NULL,
    id_rol INTEGER NOT NULL,
    FOREIGN KEY (id_rol) REFERENCES ROL(id_rol)
);