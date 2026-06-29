from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from load.load_interfaz import LoadInterfaz 
from load.load_pila import LoadInterfazPila
from load.load_conversion_infija_posfija import LoadInterfazPila

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/MenuPrincipal.ui', self)
        
        # Conectar acción del menú
        self.actionLista_Enlazada.triggered.connect(self.abrir_interfaz)
        self.actionPila_2.triggered.connect(self.abrir_interfazpila)
        self.actionConversion_Infija_Posfija.triggered.connect(self.abrir_interfazpila)
        
    def abrir_interfaz(self):
        self.interfaz = LoadInterfaz()
        self.interfaz.show()
        
    def abrir_interfazpila(self):
        self.pila = LoadInterfazPila()
        self.pila.show()
        
    def abrir_interfazconversion(self):
        self.conversion = LoadInterfazPila()
        self.conversion.show()
        
    
