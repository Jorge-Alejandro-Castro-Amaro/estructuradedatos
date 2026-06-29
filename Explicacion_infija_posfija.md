# Conversión de Expresiones Infijas a Posfijas

## ¿Qué es una expresión infija?
Es la forma común de escribir operaciones:


## ¿Qué es una expresión posfija?
Es una notación donde los operadores van después de los operandos:


## Algoritmo (Shunting Yard simplificado)
1. Leer la expresión de izquierda a derecha.
2. Si es operando → enviar a la salida.
3. Si es operador → usar la pila para decidir cuándo sacarlo.
4. Si es paréntesis → manejar apertura y cierre con la pila.
5. Al final → vaciar la pila.

## Uso de la pila
La pila se utiliza para **guardar operadores y paréntesis** mientras se procesa la expresión.  
Esto asegura que los operadores se coloquen en el orden correcto según su **prioridad**.

Ejemplo:
