from estructuras.lineales.nodo import Node

class LinkedList(object):
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

    def search(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def delete_first(self):
        if self.head is None:
            return None
        eliminado = self.head.data
        self.head = self.head.next
        if self.head is None:  # si la lista quedó vacía
            self.tail = None
        return eliminado

    def delete_last(self):
        if self.head is None:
            return None
        if self.head == self.tail:  # solo un elemento
            eliminado = self.head.data
            self.head = None
            self.tail = None
            return eliminado
        # recorrer hasta el penúltimo
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        eliminado = self.tail.data
        temp.next = None
        self.tail = temp
        return eliminado