from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from load.load_interfaz import LoadInterfaz 

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/MenuPrincipal.ui', self)
        
        # Conectar acción del menú
        self.actionLista_Enlazada.triggered.connect(self.abrir_interfaz)
        
    def abrir_interfaz(self):
        # Si quieres que el diálogo bloquee hasta que se cierre (modal):
        # self.interfaz = LoadInterfaz()
        # self.interfaz.exec_()

        # Si quieres que el diálogo se abra y la ventana principal siga activa (no modal):
        self.interfaz = LoadInterfaz()
        self.interfaz.show()
        
    
