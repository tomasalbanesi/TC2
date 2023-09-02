# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 12:08:35 2023

@title: TP5 Filtros digitales ejercicio 2)a)
@filename: Script_TP5_Ejercicio2A.py
@author: Tomas Agustin Albanesi
"""

# Importacion de modulos y funciones
import matplotlib.pyplot as plt
import scipy.signal as sig
import numpy as np
from pytc2.sistemas_lineales import pzmap

# Frecuencias
fc = 1*10**3
fs = 100*10**3

# Constantes
k = 2 * fs
C = (2*np.pi*fc)/k
CC = C**2

# Armo filtro analogico
analog_num = [(2*np.pi*fc)**2]
analog_den = [1,(np.sqrt(2)*2*np.pi*fc),(2*np.pi*fc)**2]
analog_sys = sig.TransferFunction(analog_num, analog_den)

# Armo filtro digital
digital_num = [CC,2*CC,CC]
digital_den = [(1+np.sqrt(2)*C+CC),(2*CC-2),(1+CC-np.sqrt(2)*C)]
digital_sys = sig.TransferFunction(digital_num, digital_den, dt=1/fs)

# Inicializacion de figura
fig, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True)

# Obtencion de bode
w_a, mag_a, phase_a = analog_sys.bode()
w_d, mag_d, phase_d = sig.dbode(digital_sys)

# Graficos de modulo
ax1.semilogx(w_a/(2*np.pi), mag_a, color='g', label='Analógico')
ax1.semilogx(w_d/(2*np.pi), mag_d, color='b', label='Digital') 
ax1.set_title('Función de Transferencia - Comparación analógico vs digital')
ax1.set_xlabel('Frecuencia (Hz)')
ax1.set_ylabel('Ganancia (dB)')
ax1.grid(True, which='both', axis='x', color='xkcd:light grey')
ax1.legend()

# Graficos de fase
ax2.semilogx(w_a/(2*np.pi), phase_a, color='g', label='Analógico', linestyle='dashed')
ax2.semilogx(w_d/(2*np.pi), phase_d, color='b', label='Digital', linestyle='dashed')
ax2.set_xlabel('Frecuencia (Hz)')
ax2.set_ylabel('Fase (radianes)')
ax2.grid(True, which='both', axis='x', color='xkcd:light grey')
ax2.legend()

plt.show()

# Diagrama de polos y ceros analogico
pzmap(analog_sys, fig_id=2)

# Diagrama de polos y ceros digital
pzmap(digital_sys, fig_id=3)

