from ui.menu import mostrar_menu

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            # Lógica para registrar cliente
            pass
        elif opcion == "2":
            # Lógica para registrar venta de producto
            pass
        elif opcion == "3":
            # Lógica para buscar cliente por cédula
            pass
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
    