from estructuras.lineales.lista_enlazada_simple import LinkedList

class OperacionesPila:
    def __init__(self, lista: LinkedList):
        self.lista = lista
        self.resultado = ""
        
    def pila_agregar(self, data):
        self.lista.insert_at_beginning(data)
        self.resultado = f"Elemento {data} agregado a la pila."
        return self.resultado
    
    def pila_eliminar(self):
        eliminado = self.lista.delete_first()
        if eliminado is None:
            self.resultado = "La pila está vacía, no se puede eliminar."
        else:
            self.resultado = f"Elemento {eliminado} eliminado de la pila."
        return eliminado
    
    def pila_tope(self):
        if self.lista.head is None:
            self.resultado = "La pila está vacía."
            return None
        self.resultado = f"El tope de la pila es: {self.lista.head.data}"
        return self.lista.head.data
    
    def pila_imprimir(self):
        if self.lista.head is None:
            self.resultado = "La pila está vacía."
            return self.resultado
        elementos = []
        temp = self.lista.head
        while temp is not None:
            elementos.append(str(temp.data))
            temp = temp.next
        self.resultado = " -> ".join(elementos)
        return self.resultado
    
    def is_empty(self):
        return self.lista.head is None
