from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from menus.menu_pila import OperacionesPila
from estructuras.lineales.conversion_expresiones import ConvertidorExpresiones

class LoadInterfazPila(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/conversion_infija_posfija.ui', self)

        # Ya no usamos LinkedList, solo la pila
        #self.operaciones = OperacionesPila([])  
        self.convertidor = ConvertidorExpresiones()

        # Conectar botón de conversión
        self.btn_convertir.clicked.connect(self.convertir_infija_a_posfija)
        
    def convertir_infija_a_posfija(self):
        expresion_infija = self.txt_expresion.text()
        if not expresion_infija.strip():
            self.lbl_resultado.setText("Ingrese una expresión válida.")
            return
        
        try:
            resultado_posfija = self.convertidor.infija_a_posfija(expresion_infija)
            self.lbl_resultado.setText(resultado_posfija)
        except Exception as e:
            self.lbl_resultado.setText(f"Error: {str(e)}")
