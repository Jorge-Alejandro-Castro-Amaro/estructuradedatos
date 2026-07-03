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
        # 1. Obtiene la expresión posfija que ya se mostró en la interfaz
        expresion_posfija = self.lbl_resultado.text()

        # 2. Verifica que no esté vacía. Si el usuario no ha convertido nada,
        #    muestra un mensaje en otro label (lbl_resultado_evaluar).
        if not expresion_posfija.strip():
            self.lbl_resultado_evaluar.setText("Primero convierta la expresión.")
            return

        try:
            # 3. Llama al método evaluar_posfija de tu clase ConvertidorExpresiones.
            #    Este método recorre la expresión posfija, usa la pila para apilar
            #    operandos y aplicar operaciones cuando encuentra operadores.
            resultado = self.convertidor.evaluar_posfija(expresion_posfija)

            # 4. Muestra el resultado numérico en el label lbl_resultado_evaluar.
            self.lbl_resultado_evaluar.setText(f"Resultado: {resultado}")

        except Exception as e:
            # 5. Si ocurre algún error (por ejemplo, expresión mal formada),
            #    se captura la excepción y se muestra el mensaje de error.
            self.lbl_resultado_evaluar.setText(f"Error: {str(e)}")
