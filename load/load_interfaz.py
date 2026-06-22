from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from menus.menu_lista_enlazada import OperacionesLista
from estructuras.lineales.lista_enlazada_simple import LinkedList

class LoadInterfaz(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/interfaz.ui', self)

        # Crear la lista y el controlador de operaciones
        self.lista = LinkedList()
        self.operaciones = OperacionesLista(self.lista)

        # Conectar botones
        self.btn_agregarI.clicked.connect(self.agregar_inicio)
        self.btn_agregarf.clicked.connect(self.agregar_final)
        self.btn_imprimir.clicked.connect(self.imprimir)
        self.btn_buscar.clicked.connect(self.buscar)
        self.btn_eliminari.clicked.connect(self.eliminar_inicio)
        self.btn_eliminarf.clicked.connect(self.eliminar_final)

    def agregar_inicio(self):
        dato = self.txt_dato.text()
        self.operaciones.agregar_inicio(dato)
        self.lbl_resultado.setText(self.operaciones.resultado)

    def agregar_final(self):
        dato = self.txt_dato.text()
        self.operaciones.agregar_final(dato)
        self.lbl_resultado.setText(self.operaciones.resultado)

    def imprimir(self):
        self.operaciones.mostrar()
        self.lbl_resultado.setText(self.operaciones.resultado)

    def buscar(self):
        dato = self.txt_dato.text()
        self.operaciones.buscar(dato)
        self.lbl_resultado.setText(self.operaciones.resultado)

    def eliminar_inicio(self):
        self.operaciones.eliminar_inicio()
        self.lbl_resultado.setText(self.operaciones.resultado)

    def eliminar_final(self):
        self.operaciones.eliminar_final()
        self.lbl_resultado.setText(self.operaciones.resultado)

'''
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from menus.menu_lista_enlazada import OperacionesLista   # ✅ Importamos la clase unificada
from estructuras.lineales.linkedlist import LinkedList   # ✅ Importamos la estructura de lista

class LoadInterfaz(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/interfaz.ui', self)

        # ✅ Crear la lista enlazada y el controlador de operaciones
        # Antes: no tenías esto, intentabas llamar a métodos como si fueran clases
        self.lista = LinkedList()
        self.operaciones = OperacionesLista(self.lista)

        # ✅ Conectar botones con sus funciones
        self.btn_agregarI.clicked.connect(self.agregar_inicio)
        self.btn_agregarf.clicked.connect(self.agregar_final)
        self.btn_imprimir.clicked.connect(self.imprimir)
        self.btn_buscar.clicked.connect(self.buscar)
        self.btn_eliminari.clicked.connect(self.eliminar_inicio)
        self.btn_eliminarf.clicked.connect(self.eliminar_final)

    def agregar_inicio(self):
        dato = self.txt_dato.text()   # ✅ Tomamos el texto del QLineEdit
        self.operaciones.agregar_inicio(dato)   # ✅ Usamos el método de OperacionesLista
        self.lbl_resultado.setText(self.operaciones.resultado)  # ✅ Mostramos el mensaje

    def agregar_final(self):
        dato = self.txt_dato.text()   # ✅ Igual que arriba, pero al final
        self.operaciones.agregar_final(dato)
        self.lbl_resultado.setText(self.operaciones.resultado)

    def imprimir(self):
        self.operaciones.mostrar()    # ✅ Llamamos directamente al método mostrar()
        self.lbl_resultado.setText(self.operaciones.resultado)

    def buscar(self):
        dato = self.txt_dato.text()   # ✅ Buscamos el dato ingresado
        self.operaciones.buscar(dato)
        self.lbl_resultado.setText(self.operaciones.resultado)

    def eliminar_inicio(self):
        self.operaciones.eliminar_inicio()   # ✅ Eliminamos el primer nodo
        self.lbl_resultado.setText(self.operaciones.resultado)

    def eliminar_final(self):
        self.operaciones.eliminar_final()    # ✅ Eliminamos el último nodo
        self.lbl_resultado.setText(self.operaciones.resultado)
'''