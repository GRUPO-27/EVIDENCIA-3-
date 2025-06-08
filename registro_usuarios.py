
class Usuario:
    def __init__(self, nombre, usuario, contrasena, rol):
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol

def registrar_usuario():
    nombre = input("Ingrese su nombre completo: ")
    usuario = input("Ingrese un nombre de usuario: ")
    
    usuario_existente = False
    try:
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                partes = linea.strip().split(";")
                if len(partes) > 1 and usuario == partes[1]:
                    usuario_existente = True
                    break
    except FileNotFoundError:
        pass

    if usuario_existente:
        print("Este usuario ya está registrado. Pruebe con otro")
        return
    
    while True:
        contrasena = input("Ingrese una contraseña (mínimo 6 caracteres con letras y números): ")
        if len(contrasena) < 6:
            print("La contraseña debe tener al menos 6 caracteres")
            continue
        
        if not any(c.isalpha() for c in contrasena):
            print("La contraseña debe contener al menos una letra")
            continue
            
        if not any(c.isdigit() for c in contrasena):
            print("La contraseña debe contener al menos un número")
            continue
            
        break
    
    try:
        with open("usuarios.txt", "r") as archivo:
            contenido = archivo.read()
            rol = "admin" if contenido.strip() == "" else "usuario"
    except FileNotFoundError:
        rol = "admin"
    
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{nombre};{usuario};{contrasena};{rol}\n")
    
    print(f"Usuario registrado correctamente como {rol}")
