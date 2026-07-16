from estructuras.lineales.queve import Queue
from datetime import datetime

class Cliente:
    def __init__(self, turno):
        self.turno = turno
        self.hora_ingreso = datetime.now()
        self.hora_salida = None
        self.tiempo_atencion = None

    def finalizar_atencion(self):
        self.hora_salida = datetime.now()
        diferencia = self.hora_salida - self.hora_ingreso
        self.tiempo_atencion = diferencia.total_seconds()
        return self.tiempo_atencion

    def __str__(self):
        # Mostrar turno y hora de ingreso
        return f"Cliente {self.turno} (Ingreso: {self.hora_ingreso.strftime('%d/%m/%Y %H:%M:%S')})"

class Banco:
    def __init__(self):
        self.cola = Queue()
        self.clientes_atendidos = []
        self.banco_abierto = True

    def registrar_cliente(self, turno):
        if not self.banco_abierto:
            return "El banco está cerrado, no se pueden registrar más turnos."
        cliente = Cliente(turno)
        self.cola.enqueue(cliente)
        return f"Cliente {turno} ingresó a las {cliente.hora_ingreso.strftime('%H:%M:%S')}"

    def atender_cliente(self):
        if self.cola.isEmpty():
            return None, "No hay clientes en la cola."
        
        cliente = self.cola.dequeue()
        tiempo = cliente.finalizar_atencion()
        self.clientes_atendidos.append(cliente)

        resumen = (
            f"Cliente {cliente.turno} atendido.\n"
            f"Hora ingreso: {cliente.hora_ingreso.strftime('%H:%M:%S')}\n"
            f"Hora salida: {cliente.hora_salida.strftime('%H:%M:%S')}\n"
            f"Tiempo de atención: {int(tiempo)} segundos"
        )
        return cliente, resumen

    def cerrar_banco(self):
        if not self.cola.isEmpty():
            return False, "No se puede cerrar: aún hay clientes esperando."
        
        self.banco_abierto = False
        total_clientes = len(self.clientes_atendidos)
        total_tiempo = sum(c.tiempo_atencion for c in self.clientes_atendidos)
        promedio = total_tiempo / total_clientes if total_clientes > 0 else 0

        resumen = (
            f"Banco cerrado.\n"
            f"Clientes atendidos: {total_clientes}\n"
            f"Tiempo total: {int(total_tiempo)} segundos\n"
            f"Tiempo promedio: {int(promedio)} segundos"
        )

        # 🔹 Limpiar el registro detallado de clientes
        self.clientes_atendidos.clear()

        return True, resumen
