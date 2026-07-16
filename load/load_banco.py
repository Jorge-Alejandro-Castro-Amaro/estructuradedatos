from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QDateTime
from PyQt5 import uic
from estructuras.lineales.banco import Banco

class LoadBanco(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('ui/interfaz_banco.ui', self)
        self.banco = Banco()

        # Conectar botones
        self.btn_turno.clicked.connect(self.registrar_turno)
        self.btn_atender.clicked.connect(self.atender_cliente)
        self.btn_cerrar.clicked.connect(self.cerrar_banco)
        
    def registrar_turno(self):
        if not self.banco.banco_abierto:  # 🔹 Usamos directamente la bandera del banco
            self.lbl_excepcion.setText("El banco está cerrado, no se pueden registrar más clientes.")
            return

        try:
            turno = int(self.txt_turno.text())
            self.banco.registrar_cliente(turno)

            # Mostrar todos los clientes en la cola
            elementos = []
            temp = self.banco.cola.lista.head
            while temp is not None:
                elementos.append(str(temp.data))  # usa __str__ de Cliente
                temp = temp.next
            self.lbl_turnos.setText("\n".join(elementos))

            self.txt_turno.clear()
        except ValueError:
            self.lbl_excepcion.setText("Ingresa un turno valido.")

    def atender_cliente(self):
        cliente, mensaje = self.banco.atender_cliente()
        if cliente:
            # Actualizar la cola en lbl_turnos
            elementos = []
            temp = self.banco.cola.lista.head
            while temp is not None:
                elementos.append(str(temp.data))
                temp = temp.next
            self.lbl_turnos.setText("\n".join(elementos))

            # Mostrar datos del cliente atendido con hora
            hora_actual = QDateTime.currentDateTime().toString("hh:mm:ss")
            self.lbl_hrsalida.setText(f"{mensaje}\nHora atención: {hora_actual}")
        else:
            self.lbl_excepcion.setText(mensaje)

    def cerrar_banco(self):
        exito, mensaje = self.banco.cerrar_banco()
        self.lbl_excepcion.setText(mensaje)

        # 🔹 Siempre bloquear ingreso de nuevos clientes
        self.txt_turno.setEnabled(False)
        self.btn_turno.setEnabled(False)

        if exito:
            # Banco cerrado correctamente (cola vacía)
            self.lbl_turnos.setText("Banco cerrado correctamente.")
            self.lbl_hrsalida.clear()
        else:
            # Banco no se puede cerrar porque aún hay clientes
            self.lbl_turnos.setText("Banco cerrado para nuevos ingresos.\nSolo se atenderán los clientes en espera.")
