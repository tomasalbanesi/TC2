# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 21:48:42 2023

@author: tomas
"""

import numpy as np
import matplotlib.pyplot as plt

# Definir una señal continua (por ejemplo, una señal senoidal)
fmax = 10  # Frecuencia máxima de la señal en Hz
t = np.linspace(0, 1, 1000)  # Tiempo de 0 a 1 segundo
signal = np.sin(2 * np.pi * fmax * t)

# Configurar la figura para mostrar la señal continua
plt.figure(figsize=(10, 4))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Señal Continua")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

# Definir tasas de muestreo
sample_rates = [30]  # Diferentes tasas de muestreo en Hz

# Muestrear la señal a diferentes tasas de muestreo y mostrarlas
plt.subplot(2, 1, 2)
for Fs in sample_rates:
    Ts = 1 / Fs  # Período de muestreo
    n = np.arange(0, 1, Ts)
    sampled_signal = np.sin(2 * np.pi * fmax * n)
    plt.stem(n, sampled_signal, label=f'Fs = {Fs} Hz', basefmt=" ", use_line_collection=True)

plt.title("Señales Muestreadas")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()

plt.tight_layout()
plt.show()
