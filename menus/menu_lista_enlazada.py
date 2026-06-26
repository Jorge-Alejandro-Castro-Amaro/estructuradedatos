from estructuras.lineales.lista_enlazada_simple import LinkedList

class OperacionesLista:
    def __init__(self, lista: LinkedList):
        self.lista = lista
        self.resultado = ""

    def agregar_inicio(self, dato):
        self.lista.insert_at_beginning(dato)
        self.resultado = f"Elemento '{dato}' agregado al inicio de la lista."

    def agregar_final(self, dato):
        self.lista.insert_at_end(dato)
        self.resultado = f"Elemento '{dato}' agregado al final de la lista."

    def buscar(self, dato):
        encontrado = self.lista.search(dato)
        if encontrado:
            self.resultado = f"Elemento '{dato}' encontrado en la lista."
        else:
            self.resultado = f"Elemento '{dato}' no encontrado en la lista."

    def mostrar(self):
        contenido = []
        current = self.lista.head
        while current:
            contenido.append(str(current.data))
            current = current.next
        self.resultado = " -> ".join(contenido) if contenido else "La lista está vacía."

    def eliminar_inicio(self):
        eliminado = self.lista.delete_first()
        if eliminado:
            self.resultado = f"Elemento '{eliminado}' eliminado del inicio de la lista."
        else:
            self.resultado = "La lista está vacía. No hay elementos para eliminar."

    def eliminar_final(self):
        eliminado = self.lista.delete_last()
        if eliminado:
            self.resultado = f"Elemento '{eliminado}' eliminado del final de la lista."
        else:
            self.resultado = "La lista está vacía. No hay elementos para eliminar."
            

