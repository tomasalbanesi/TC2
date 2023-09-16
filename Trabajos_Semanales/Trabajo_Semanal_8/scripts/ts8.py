# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 09:48:04 2023

@author: tomas
"""

# Inicialización e importación de módulos

# Módulos importantantes
import scipy.signal as sig
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.io as sio
from pytc2.sistemas_lineales import plot_plantilla

fs = 1000 # Hz
nyq_frec = fs / 2

# Plantilla

# filter design
ripple = 0.5 # dB
atenuacion = 40 # dB

ws1 = 1.0 #Hz
wp1 = 3 #Hz
wp2 = 25.0 #Hz
ws2 = 35.0 #Hz

frecs = np.array([0.0,         ws1,         wp1,     wp2,     ws2,         nyq_frec   ]) / nyq_frec
gains = np.array([-atenuacion, -atenuacion, -ripple, -ripple, -atenuacion, -atenuacion])
gains = 10**(gains/20)

# b, a = sig.iirdesign(wp = [wp1/nyq_frec, wp2/nyq_frec], ws = [ws1/nyq_frec, ws2/nyq_frec], gpass = 0.5, gstop = 40, analog=False, ftype='butter', fs = fs)      

# frecuencias = np.linspace(0, nyq_frec, num = fs)

# w, h = sig.freqz(b, a, frecuencias, fs = fs)

# fig, ax1 = plt.subplots()
# ax1.set_title('Digital filter frequency response')
# ax1.plot(w, 20 * np.log10(np.abs(h)), 'b')
# ax1.set_ylabel('Amplitude [dB]', color='b')
# ax1.set_xlabel('Frequency [rad/sample]')

# ax2 = ax1.twinx()
# angles = np.unwrap(np.angle(h))
# ax2.plot(w, angles, 'g')
# ax2.set_ylabel('Angle (radians)', color='g')
# ax2.grid(True)
# ax2.axis('tight')
# plt.show()

bp_sos_butter = sig.iirdesign(wp = [wp1/nyq_frec, wp2/nyq_frec], ws = [ws1/nyq_frec, ws2/nyq_frec], gpass = 0.5, gstop = 40, analog=False, ftype='butter', output='sos')      

frecuencias = np.linspace(0.5, 100, num = 10000)

w, h = sig.sosfreqz(bp_sos_butter, frecuencias, fs = fs)

fig, ax1 = plt.subplots()
ax1.set_title('Digital filter frequency response IIR')
ax1.plot(w, 20 * np.log10(np.abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [Hz]')
ax1.grid()

ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
ax2.plot(w, angles, 'g')
ax2.set_ylabel('Angle (radians)', color='g')
ax2.grid(True)
ax2.axis('tight')
plt.show()

plot_plantilla(filter_type = 'bandpass', fpass = frecs[[2, 3]]* nyq_frec, ripple = ripple , fstop = frecs[ [1, 4] ]* nyq_frec, attenuation = atenuacion, fs = fs)

################### FIR UNIFICADO ###########################

cant_coeficientes = 1501

num_win = sig.firwin2(cant_coeficientes, frecs, gains , window='blackmanharris')

den = 1.0

# muestreo el filtro donde me interesa verlo según la plantilla.
w  = np.append(np.logspace(-1, 0.8, 250), np.logspace(0.9, 1.6, 250) )
w  = np.append(w, np.linspace(110, nyq_frec, 100, endpoint=True) ) / nyq_frec * np.pi

_, hh_win = sig.freqz(num_win, den, w)

# renormalizo el eje de frecuencia
w = w / np.pi * nyq_frec

plt.plot(w, 20 * np.log10(abs(hh_win)), label='FIR-Win {:d}'.format(num_win.shape[0]))

plt.title('Filtros diseñados')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Módulo [dB]')
plt.grid()
plt.axis([0, 100, -60, 5 ]);

axes_hdl = plt.gca()
axes_hdl.legend()

plot_plantilla(filter_type = 'bandpass', fpass = frecs[[2, 3]]* nyq_frec, ripple = ripple , fstop = frecs[ [1, 4] ]* nyq_frec, attenuation = atenuacion, fs = fs)

################### FIR SEPARADO ###########################

wpmed = 12
cant_coeficientes1 = 1501
cant_coeficientes2 = 501

frecs1 = np.array([0.0        ,         ws1,         wp1,    nyq_frec   ]) / nyq_frec
gains1 = np.array([0, -atenuacion, -ripple, 0])
gains1 = 10**(gains1/20)

num1_win = sig.firwin2(cant_coeficientes1, frecs1, gains1 , window='blackmanharris', antisymmetric=True)

den = 1.0

# muestreo el filtro donde me interesa verlo según la plantilla.
w  = np.append(np.logspace(-1, 0.8, 250), np.logspace(0.9, 1.6, 250) )
w  = np.append(w, np.linspace(110, nyq_frec, 100, endpoint=True) ) / nyq_frec * np.pi

_, hh1_win = sig.freqz(num1_win, den, w)

# renormalizo el eje de frecuencia
w = w / np.pi * nyq_frec

plt.plot(w, 20 * np.log10(abs(hh1_win)), label='FIR-Win {:d}'.format(num_win.shape[0]))

plt.title('Filtros diseñados')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Módulo [dB]')
plt.grid()
plt.axis([0, 100, -60, 5 ]);

axes_hdl = plt.gca()
axes_hdl.legend()