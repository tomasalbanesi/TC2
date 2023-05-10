# -*- coding: utf-8 -*-
"""
Created on Thu May  4 10:53:53 2023

@author: talbanesi
"""

# Importacion de librerias
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
# from splane import analyze_sys # version vieja
from pytc2.sistemas_lineales import analyze_sys

# Definicion de atenuacion maxima en db
alfa_max = 1

# Definicion de frecuencia angular de banda de stop
ws = 2

# cuentas auxiliares

# Calculo de Epsilon Cuadrado, idem para maxima planicidad y Cheby
ee = 10**(alfa_max/10)-1

# Itero para calcular el n del filtro
for nn in range(2,9):
    
    # Calculo de atenuacion minima en db para maxima planicidad
    alfa_min_b = 10*np.log10(1 + ee * ws**(2*nn))
    
    # Calculo de atenuacion minima en db para chebyshev 
    alfa_min_c = 10*np.log10(1 + ee * np.cosh(nn * np.arccosh(ws))**2 )
    
    # Muestro los resultados
    print( 'nn {:d} - alfa_min_butter {:f} - alfa_min_cheby {:f}'.format(nn, alfa_min_b, alfa_min_c) )


# Elijo un orden luego de iterar ... suponiendo que me solicitaron una determinada atenuacion
nn = 2

### Verificación Maxima Planicidad

# sig.buttap(nn) -> Funcion para obtener ceros, polos y ganancia de una transferencia tipo Butterworth, pasandole el orden
z,p,k = sig.buttap(nn)

# Obtengo la transferencia, a partir de los ceros, polos y ganancia
num, den = sig.zpk2tf(z,p,k)

# Aplico la renormalización a \omega_butter (conversion lowpass a lowpass, modificando la frecuencia)
num_mp, den_mp = sig.lp2lp(num, den, ee**(-1/(2*nn)))

### Verificación Chebyshev
z,p,k = sig.cheb1ap(nn, alfa_max)
num_cheb, den_cheb = sig.zpk2tf(z,p,k)

### Análisis de respuesta en frecuencia

# Creo array con las transferencias
all_sys = [sig.TransferFunction(num_mp, den_mp), 
           sig.TransferFunction(num_cheb, den_cheb)]

# Agrego los nombres de los filtros
filter_names = ['MP_' + str(nn) + '_ripp_' + str(alfa_max) + 'dB',
                'Cheb_' + str(nn) + '_ripp_' + str(alfa_max) + 'dB']

plt.close('all')

# Funcion de splane para analizar sistemas (grafica modulo, fase, diagrama de polos y ceros, retardo de grupo)
analyze_sys(all_sys, filter_names)

