# -*- coding: utf-8 -*-
"""
Created on Thu May  4 11:43:23 2023

@author: talbanesi
"""

# Importacion de librerias
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
# from splane import analyze_sys # version vieja
from pytc2.sistemas_lineales import analyze_sys

plt.close("all")

### DATOS DE PLANTILLA (parametros a modificar)

# Definicion de atenuacion maxima en db
alfa_max = 0.5
# Definicion de atenuacion minima en db
alfa_min = 20
# Definicion de frecuencia angular de banda de stop normalizada
ws = 3.83
# Definicion de frecuencia angular de banda de paso normalizada
wp = 1

# Calculo de Epsilon Cuadrado, idem para maxima planicidad y Cheby
ee = 10**(alfa_max/10)-1

# Itero para calcular el n del filtro
veces = 0
for nn in range(1,9):
    
    # Calculo de atenuacion minima en db para chebyshev 
    alfa_min_n = 10*np.log10(1 + ee * np.cosh(nn * np.arccosh(ws))**2 )
    
    # Muestro los resultados
    print( 'nn {:d} - alfa_min_cheby {:f}'.format(nn, alfa_min_n) )
    
    if (alfa_min_n > alfa_min and veces == 0):
        
        n_seleccionado = nn
        veces = veces + 1
        
num = [0.49]
den = [1, 0.986, 1.235, 0.49]
filtro = sig.TransferFunction(num, den)

analyze_sys(filtro)        

num = [1, 0, 0, 0]
den = [1, 2.52, 2.01, 2.04]
filtro = sig.TransferFunction(num, den)

analyze_sys(filtro)