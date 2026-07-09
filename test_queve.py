from estructuras.lineales.queve import Queue

def menu():
    print("\n=== MENÚ DE PRUEBA PARA COLA ===")
    print("1. Enqueue (agregar elemento)")
    print("2. Dequeue (eliminar elemento)")
    print("3. FirstQueue (consultar primero)")
    print("4. LastQueue (consultar último)")
    print("5. PrintQueue (mostrar cola)")
    print("6. IsEmpty (verificar si está vacía)")
    print("0. Salir")

def test_queue_interactivo():
    cola = Queue()
    opcion = -1

    while opcion != 0:
        menu()
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Debes ingresar un número válido.")
            continue

        if opcion == 1:
            valor = input("Ingresa el valor a encolar: ")
            cola.enqueue(valor)
            print(cola.resultado)

        elif opcion == 2:
            eliminado = cola.dequeue()
            print(cola.resultado)

        elif opcion == 3:
            primero = cola.firstQueue()
            print(cola.resultado)

        elif opcion == 4:
            ultimo = cola.lastQueue()
            print(cola.resultado)

        elif opcion == 5:
            print("Contenido de la cola:", cola.printQueue())

        elif opcion == 6:
            if cola.isEmpty():
                print("La cola está vacía.")
            else:
                print("La cola tiene elementos.")

        elif opcion == 0:
            print("Saliendo del programa...")

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    test_queue_interactivo()
