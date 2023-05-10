# -*- coding: utf-8 -*-
"""
Created on Mon May  8 18:36:58 2023

@author: talbanesi
"""

# Importacion de librerias
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
# from splane import analyze_sys # version vieja
from pytc2.sistemas_lineales import analyze_sys
from sympy import Symbol

### Definicion de datos de plantilla

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
e = np.sqrt(ee)

# Itero para calcular el n del filtro, y selecciono el primero que cruce la atenuacion minima
veces = 0
for nn in range(1,9):
    
    # Calculo de atenuacion minima en db para chebyshev 
    alfa_min_n = 10*np.log10(1 + ee * np.cosh(nn * np.arccosh(ws))**2 )
    
    # Muestro los resultados
    print( 'nn {:d} - alfa_min_cheby {:f}'.format(nn, alfa_min_n) )
    
    if (alfa_min_n > alfa_min and veces == 0):
        
        n_seleccionado = nn
        veces = veces + 1
        
print('El orden del filtro seleccionado, en base a la atenuacion minima, es: {:d}'.format(n_seleccionado))

num = [0, 0, 0, 0, 0, 0.2012]
den = [1, 0, 1.25, 0, 0.3125, 0.2012]

sys = sig.TransferFunction(num, den)

# Agrego los nombres de los filtros
# filter_name = 'MP_' + str(nn) + '_ripp_' + str(alfa_max) + 'dB'

plt.close('all')

# Funcion de splane para analizar sistemas (grafica modulo, fase, diagrama de polos y ceros, retardo de grupo)
analyze_sys(sys)

rr = np.roots(den)

s = Symbol('s')
poli2_1 = (s + rr[0]) * (s + rr[1])