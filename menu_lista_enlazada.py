from estructuras.lineales.nodo import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def print_linked_list(self):
        temp = self.head
        print("Head ->", end="")
        while temp is not None:
            print(temp.data, "->", end="")
            temp = temp.next
        print("<- Tail")
        
    def search(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next
        return False


# ---------------- MENÚ EN CONSOLA ----------------
def menu():
    lista = LinkedList()
    
    while True:
        print("\n--- MENÚ LISTA ENLAZADA ---")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Mostrar lista")
        print("4. Buscar elemento")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            dato = input("Ingresa el dato: ")
            lista.insert_at_beginning(dato)
            print("Dato insertado al inicio.")

        elif opcion == "2":
            dato = input("Ingresa el dato: ")
            lista.insert_at_end(dato)
            print("Dato insertado al final.")

        elif opcion == "3":
            lista.print_linked_list()

        elif opcion == "4":
            dato = input("Dato a buscar: ")
            if lista.search(dato):
                print("El dato está en la lista.")
            else:
                print("l dato NO está en la lista.")

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida, intenta de nuevo.")

# Ejecutar menú
menu()
