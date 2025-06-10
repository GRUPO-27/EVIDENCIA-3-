def iniciar_sesion():
    usuario_input = input("Ingrese su nombre de usuario: ")
    contrasena_input = input("Ingrese su contraseña: ")

    try:
        with open("usuarios.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(";")
                if len(partes) != 4:
                    continue  
                nombre, usuario, contrasena, rol = partes
                if usuario_input == usuario and contrasena_input == contrasena:
                    print(f"Inicio de sesión exitoso. Bienvenido {nombre} ({rol})")
                    return {"nombre": nombre, "usuario": usuario, "contrasena": contrasena, "rol": rol}
            print("Usuario o contraseña incorrectos.")
    except FileNotFoundError:
        print("No hay usuario registrado")
