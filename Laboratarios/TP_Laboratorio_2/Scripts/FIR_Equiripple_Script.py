# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 10:16:14 2023

@author: talbanesi
"""

# Importacion de librerias
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from scipy import signal as sig
from pytc2.sistemas_lineales import analyze_sys, pretty_print_bicuad_omegayq, plot_plantilla

# Funcion para obtener el retardo de grupo
def group_delay(ww, phase):
    
    groupDelay = -np.diff(phase)/np.diff(ww)
    
    return(np.append(groupDelay, groupDelay[-1]))

# Plantilla
f_pass = 1e3
f_stop = 2e3
at_pass = 1
at_stop = 20
fs = 40e3
f_nyq = fs/2

# Coeficientes
num_fir = np.array([0.012833854796107356,-0.01502735492128993,-0.01179378971652337,-0.010974556063682445,-0.011145717068024634,-0.011522031520490587,-0.011632154328911487,-0.01118083415626888,-0.009972608695541535,-0.007870754776516047,-0.004797227569706377,-0.0007341532225183175,0.004286970799681492,0.010189377198560546,0.016847299061108736,0.024087491013086954,0.03169237253219173,0.03940385214683914,0.04694547035904183,0.054055029557683335,0.06048508223903896,0.0659754847122731,0.0702751650699014,0.07324679013529431,0.0747775735272231,0.0747775735272231,0.07324679013529431,0.0702751650699014,0.0659754847122731,0.06048508223903896,0.054055029557683335,0.04694547035904183,0.03940385214683914,0.03169237253219173,0.024087491013086954,0.016847299061108736,0.010189377198560546,0.004286970799681492,-0.0007341532225183175,-0.004797227569706377,-0.007870754776516047,-0.009972608695541535,-0.01118083415626888,-0.011632154328911487,-0.011522031520490587,-0.011145717068024634,-0.010974556063682445,-0.01179378971652337,-0.01502735492128993,0.012833854796107356])
den_fir = 1

# Vector de frecuencias
w = np.logspace(-4, 4, 1000) / f_nyq * np.pi

# Respuesta en frecuencia
_, h = sig.freqz(num_fir, den_fir, w)

w = w / np.pi * f_nyq

# Modulo
plt.title('Filtros diseñados')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Módulo [dB]')
plt.plot(w, 20 * np.log10(np.abs(h)), label='FIR')
plt.legend('FIR')
plot_plantilla(filter_type = 'lowpass', fpass = f_pass, ripple = at_pass , fstop = f_stop, attenuation = at_stop, fs = fs)

# Fase
plt.figure()
plt.title('Respuesta de fase FIR')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Ángulo [rad]')
fase_fir = np.unwrap(np.angle(h))
plt.plot(w, fase_fir)
plt.grid(which='both', axis='both')


# Retardo de grupo
gd_iir = group_delay(w, fase_fir)
plt.figure()
plt.title('Retardo de grupo FIR')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Demora [s]')
plt.plot(w, gd_iir)
plt.grid(which='both', axis='both')
