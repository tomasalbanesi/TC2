# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:09:23 2023

@author: talbanesi
"""

# Importacion de librerias
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
import matplotlib as mpl
from pytc2.sistemas_lineales import pzmap, bodePlot, tf2sos_analog, analyze_sys, parametrize_sos, pretty_print_lti, pretty_print_bicuad_omegayq, tf2sos_analog, pretty_print_SOS
from IPython.display import display, Markdown

plt.close("all")

### DATOS DE PLANTILLA (parametros a modificar)

# Definicion de atenuacion maxima en db
alfa_max = 1
# Definicion de atenuacion minima en db
alfa_min = 20
# Definicion de frecuencia angular de banda de stop normalizada
ws = 3.83
# Definicion de frecuencia angular de banda de paso normalizada
wp = 1

# Calculo de Epsilon Cuadrado, idem para maxima planicidad y Cheby
ee = 10**(alfa_max/10)-1
print( 'Epsilon^2 ee = {:f}'.format(ee))

# Itero para calcular el n del filtro
veces = 0
for nn in range(1,5):
    
    # Calculo de atenuacion minima en db para chebyshev 
    alfa_min_n = 10*np.log10(1 + ee * np.cosh(nn * np.arccosh(ws))**2 )
    
    # Muestro los resultados
    print( 'nn {:d} - alfa_min_cheby {:f}'.format(nn, alfa_min_n) )
    
    if (alfa_min_n > alfa_min and veces == 0):
        
        n_seleccionado = nn
        veces = veces + 1
        
print('Seleccionamos el orden nn {:d}'.format(n_seleccionado))

# Definicion de Chebyshev pasa altos prototipo
numlp, denlp = sig.cheby1(n_seleccionado, alfa_max, wp, analog=True)

# Creacion de la funcion transferencia pasa bajos prototipo
tf_lp = sig.TransferFunction(numlp, denlp)

# Conversion de pasa bajos a pasa altos
numhp, denhp = sig.lp2hp(numlp, denlp, wp)

# Creacion de la funcion transferencia pasa altos
tf_hp = sig.TransferFunction(numhp, denhp)

# Graficos

analyze_sys([tf_lp, tf_hp], ['Pasa bajos prototipo', 'Pasa altos'])


