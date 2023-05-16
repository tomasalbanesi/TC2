# -*- coding: utf-8 -*-
"""
Created on Thu May 11 10:34:55 2023

@author: talbanesi
"""

# Importacion de librerias
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
# from splane import analyze_sys # version vieja
from pytc2.sistemas_lineales import analyze_sys


### DATOS DE PLANTILLA (parametros a modificar)

# Definicion de atenuacion maxima en db
alfa_max = 0.4
# Definicion de atenuacion minima en db
alfa_min = 48
# Definicion de frecuencia angular de banda de stop normalizada
ws = 3
# Definicion de frecuencia angular de banda de paso normalizada
wp = 1

# Calculo de Epsilon Cuadrado, idem para maxima planicidad y Cheby
ee = 10**(alfa_max/10)-1

# Itero para calcular el n del filtro
veces = 0
for nn in range(2,9):
    
    # Calculo de atenuacion minima en db para chebyshev 
    alfa_min_n = 10*np.log10(1 + ee * np.cosh(nn * np.arccosh(ws))**2 )
    
    # Muestro los resultados
    print( 'nn {:d} - alfa_min_cheby {:f}'.format(nn, alfa_min_n) )
    
    if (alfa_min_n > alfa_min and veces == 0):
        
        n_seleccionado = nn
        veces = veces + 1
        
# Calculo los coeficientes con funciones de alto nivel
z, p, k = sig.cheb1ap(5, 0.4)
print("Los ceros son: {z}", z)
print("Los polos son: {p}", p)
print("El K es: {k}", k)