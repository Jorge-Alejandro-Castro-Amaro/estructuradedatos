from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from menus.menu_pila import OperacionesPila
from estructuras.lineales.lista_enlazada_simple import LinkedList

class LoadInterfazPila(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/interfaz_pila.ui', self)

        # Crear la lista y el controlador de operaciones
        self.lista = LinkedList()
        self.operaciones = OperacionesPila(self.lista)

        # Conectar botones
        self.btn_pop.clicked.connect(self.pila_eliminar)
        self.btn_print.clicked.connect(self.pila_print)
        self.btn_push.clicked.connect(self.pila_agregar)
        self.btn_top.clicked.connect(self.pila_tope)

    def pila_agregar(self):
        dato = self.txt_dato.text()
        if dato.strip() == "":
            self.lbl_resultado.setText("Ingrese un dato válido.")
            return
        self.operaciones.pila_agregar(dato)
        self.lbl_resultado.setText(self.operaciones.resultado)

    def pila_eliminar(self):
        eliminado = self.operaciones.pila_eliminar()
        self.lbl_resultado.setText(self.operaciones.resultado)

    def pila_print(self):
        resultado = self.operaciones.pila_imprimir()
        self.lbl_resultado.setText(resultado)

    def pila_tope(self):
        tope = self.operaciones.pila_tope()
        self.lbl_resultado.setText(self.operaciones.resultado)
