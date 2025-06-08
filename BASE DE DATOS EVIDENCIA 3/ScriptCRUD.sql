
INSERT INTO usuario (id_usuario, nombre, nombre_usuario, contrasena, id_rol) VALUES (1, 'Juan Perez', 'juanpperez11', 'Mi_Clave193', 2);

INSERT INTO Rol (id_rol, nombre_rol) VALUES (1, 'Administrador');

SELECT * FROM Rol

INSERT INTO Rol (id_rol, nombre_rol) VALUES (2, 'Usuario');

SELECT * FROM Rol

UPDATE usuario SET nombre = 'Juan Pérez', nombre_usuario = 'jperez', contrasena = 'Miclave1235', id_rol = 2 WHERE id_usuario = 1;

SELECT * FROM usuario

UPDATE usuario SET nombre = 'Juan Emilio Pérez' WHERE id_usuario = 1;

SELECT * FROM usuario

INSERT INTO usuario (nombre, nombre_usuario, contrasena, id_rol) VALUES ('Carla Rodriguez', 'CarlaRod34', 'Clavesecreta234', 1);
INSERT INTO usuario (nombre, nombre_usuario, contrasena, id_rol) VALUES ('Jorge Ceballos', 'Jorge489', 'Claveoculta345', 2);

SELECT * FROM usuario

DELETE FROM usuario WHERE id_usuario = 3;

SELECT * FROM usuario;