import inicio_sesion
import registro_usuarios

def main():
    while True:
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inicio_sesion.iniciar_sesion()
        elif opcion == "2":
            registro_usuarios.registrar_usuario()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()