from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from menus.menu_pila import OperacionesPila
from estructuras.lineales.conversion_expresiones import ConvertidorExpresiones

class LoadInterfazPila(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/conversion_infija_posfija.ui', self)
        self.convertidor = ConvertidorExpresiones()

        self.btn_convertir.clicked.connect(self.convertir_infija_a_posfija)
        self.btn_evaluar.clicked.connect(self.evaluar_posfija)

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

    def evaluar_posfija(self):
        expresion_posfija = self.lbl_resultado.text()
        if not expresion_posfija.strip():
            self.lbl_resultado_evaluar.setText("Primero convierta la expresión.")
            return
        try:
            resultado = self.convertidor.evaluar_posfija(expresion_posfija)
            self.lbl_resultado_evaluar.setText(f"Resultado: {resultado}")
        except Exception as e:
            self.lbl_resultado_evaluar.setText(f"Error: {str(e)}")