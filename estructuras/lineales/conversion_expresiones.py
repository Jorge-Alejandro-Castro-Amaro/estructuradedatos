from estructuras.lineales.stack import OperacionesPila
from estructuras.lineales.lista_enlazada_simple import LinkedList

class ConvertidorExpresiones:
    def __init__(self):
        self.pila = OperacionesPila(LinkedList())
        
    def prioridad(self, operador):
        if operador == '$':   # Potencia
            return 3
        if operador in ('*', '/'):
            return 2
        if operador in ('+', '-'):
            return 1
        return 0
    
    def infija_a_posfija(self, expresion):
        salida = []
        for token in expresion:
            if token.isalnum():
                salida.append(token)
            elif token == '(':
                self.pila.pila_agregar(token)
            elif token == ')':
                while not self.pila.is_empty() and self.pila.pila_tope() != '(':
                    salida.append(self.pila.pila_eliminar())
                self.pila.pila_eliminar()
            else:
                while (not self.pila.is_empty() and 
                       self.prioridad(self.pila.pila_tope()) >= self.prioridad(token)):
                    salida.append(self.pila.pila_eliminar())
                self.pila.pila_agregar(token)

        while not self.pila.is_empty():
            salida.append(self.pila.pila_eliminar())

        return " ".join(salida)

    def evaluar_posfija(self, expresion_posfija: str):
        # Reiniciar pila
        self.pila = OperacionesPila(LinkedList())
        
        for token in expresion_posfija.split():
            if token.isdigit():  # Operando
                self.pila.pila_agregar(int(token))
            else:  # Operador
                op2 = self.pila.pila_eliminar()
                op1 = self.pila.pila_eliminar()
                
                if token == '+':
                    self.pila.pila_agregar(op1 + op2)
                elif token == '-':
                    self.pila.pila_agregar(op1 - op2)
                elif token == '*':
                    self.pila.pila_agregar(op1 * op2)
                elif token == '/':
                    self.pila.pila_agregar(op1 // op2)  # División entera
                elif token == '$':
                    self.pila.pila_agregar(op1 ** op2)  # Potencia

        return self.pila.pila_eliminar()
    



#PDF, EXPLICACION, PROMTS, EVIDENCIA