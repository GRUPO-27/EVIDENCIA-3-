def iniciar_sesion():
    usuario_input = input("Ingrese su nombre de usuario: ")
    contrasena_input = input("Ingrese su contraseña: ")

    try:
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                nombre, usuario, contrasena, rol = linea.strip().split(";")
                if usuario_input == usuario and contrasena_input == contrasena:
                    print(f"Inicio de sesión exitoso. Bienvenido {nombre} ({rol})")
                    return Usuario(nombre, usuario, contrasena, rol)
            print("Usuario o contraseña incorrectos.")
    except FileNotFoundError:
        print("No hay usuario registrado")