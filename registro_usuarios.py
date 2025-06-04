usuarios = []

class Usuario:
    def __init__(self, nombre, nombre_usuario, contrasena, rol):
        self.nombre = nombre
        self.usuario = nombre_usuario
        self.contrasena = contrasena
        self.rol = rol

def contrasena_valida(contrasena):
    if len(contrasena) < 6:
        return False, "La contraseña debe tener al menos 6 caracteres"
    
    tiene_letra = any(char.isalpha() for char in contrasena)
    if not tiene_letra:
        return False, "La contraseña debe tener al menos una letra"
    
    tiene_numero = any(char.isdigit() for char in contrasena)
    if not tiene_numero:
        return False, "La contraseña debe tener al menos un número"
    
    return True, "Contraseña aprobada"

def registrar_usuario():
    nombre = input("Ingrese su nombre completo: ")
    nombre_usuario = input("Ingrese un nombre de usuario: ")
    
    for usuario in usuarios:
        if usuario.usuario == nombre_usuario:
            print("Ese usuario ya se encuentra registrado. Pruebe con otro")
            return

    contrasena = input("Ingrese una contraseña: ")
    es_valida, mensaje = contrasena_valida(contrasena)
    if not es_valida:
        print("Error:", mensaje)
        return
    
    nuevo_usuario = Usuario(nombre, nombre_usuario, contrasena, "usuario")
    usuarios.append(nuevo_usuario)
    
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{nombre};{nombre_usuario};{contrasena};usuario\n")
    
    print("Usuario registrado correctamente.")
    


