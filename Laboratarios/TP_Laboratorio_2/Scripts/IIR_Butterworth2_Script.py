# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 10:45:12 2023

@author: talbanesi
"""

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from scipy import signal as sig
from pytc2.sistemas_lineales import analyze_sys, pretty_print_bicuad_omegayq, plot_plantilla

def group_delay(ww, phase):
    
    groupDelay = -np.diff(phase)/np.diff(ww)
    

# Plantilla
f_pass = 1e3
f_stop = 6e3
at_pass = 1
at_stop = 20
fs = 40e3
f_nyq = fs/2

# Coeficientes
num_iir = np.array([0.010419890902565022,0.020839781805130044,0.010419890902565022])
den_iir = np.array([1.0,-1.6911935001269052,0.7328730637371653])

w = np.logspace(-4, 4, 1000) / f_nyq * np.pi

_, h = sig.freqz(num_iir, den_iir, w)

w = w / np.pi * f_nyq

# Modulo
#plt.axis([0, 100, -60, 5 ]);
plt.title('Filtros diseñados')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Módulo [dB]')
plt.plot(w, 20 * np.log10(np.abs(h)), label='IIR')
plt.legend('IIR')
plot_plantilla(filter_type = 'lowpass', fpass = f_pass, ripple = at_pass , fstop = f_stop, attenuation = at_stop, fs = fs)

# Fase
plt.figure()
plt.title('Respuesta de fase IIR')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Ángulo [rad]')
#fase_iir = np.unwrap(np.angle(h))
fase_iir = np.angle(h)
plt.plot(w, fase_iir)
plt.grid(which='both', axis='both')
#plt.xlim(0, 100)
#plt.axis([0, 100, -25, 5 ]);

# Retardo
gd_iir = group_delay(w, fase_iir)
plt.figure()
plt.title('Retardo de grupo IIR')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Demora [s]')
plt.plot(w, gd_iir)
plt.grid(which='both', axis='both')
#plt.xlim(0, 100)
#plt.axis([0, 100, -2, 7 ]);