# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Importamos Sympy
import sympy
import numpy as np
from IPython.display import display

# Obtenes los dos polinomios introducidos por el usuario
P1 = input("Primer Polinomio: ")
P2 = input("Segundo Polinomio: ")
print("n")

# Definimos los simbolos con la funcion symbols de sympy
sympy.init_printing()
x,y = sympy.symbols('x, y')

# Luego almacenamos en variables los dos polinomios procesados por la función Poly de sympy 
Poly1 = sympy.Poly(P1)
Poly2 = sympy.Poly(P2)

# Declaramos una función para cada operación que queramos utilizar
def mult(p1, p2):
    return p1 * p2
def suma(p1, p2):
    return p1 + p2
def res(p1, p2):
    return p1 - p2
def div(p1, p2):
    return p1 / p2

# Mostramos el valor que deseemos
print("Resultado: ", mult(Poly1, Poly2))

display(sympy.latex(mult(Poly1, Poly2)))