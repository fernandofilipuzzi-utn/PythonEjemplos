
def mostrar_menu():
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Salir")

def opcion_1():
    print("Has seleccionado la Opción 1.")

def opcion_2():
    print("Has seleccionado la Opción 2.")

while True:
    mostrar_menu()

    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        opcion_1()
    elif opcion == "2":
        opcion_2()
    elif opcion == "3":
        print("Saliendo")
        break
    else:
        print("Opción no válida.")