from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from load.load_interfaz import LoadInterfaz 
from load.load_pila import LoadInterfazPila, LoadInterfazPila
from load.load_conversion_infija_posfija import LoadInterfazConversion
from load.load_queue import LoadInterfazQueue
from load.load_banco import LoadBanco

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/MenuPrincipal.ui', self)
        
        # Conectar acción del menú
        self.actionLista_Enlazada.triggered.connect(self.abrir_interfaz)
        self.actionPila_2.triggered.connect(self.abrir_interfazpila)
        self.actionConversion_Infija_Posfija.triggered.connect(self.abrir_conversion)
        self.actionQueue.triggered.connect(self.abrir_interfaz_queue)
        self.actionBanco.triggered.connect(self.abrir_interfaz_banco)
        
    def abrir_interfaz(self):
        self.interfaz = LoadInterfaz()
        self.interfaz.show()
        
    def abrir_interfazpila(self):
        self.pila = LoadInterfazPila()
        self.pila.show()
        
    def abrir_conversion(self):
        self.conversion = LoadInterfazConversion()
        self.conversion.show()
        
    def abrir_interfaz_queue(self):
        self.queue = LoadInterfazQueue()
        self.queue.show()
        
    def abrir_interfaz_banco(self):
        self.banco = LoadBanco()
        self.banco.show()
        
        
    
