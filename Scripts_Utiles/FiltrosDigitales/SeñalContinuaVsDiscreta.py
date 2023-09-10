# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 21:27:31 2023

@author: tomas
"""

import numpy as np
import matplotlib.pyplot as plt

frecuencia_senoidal = 5  # Frecuencia de la señal senoidal en Hz
amplitud_senoidal = 1.0
periodo_senoidal = 1 / frecuencia_senoidal  # Periodo de la señal senoidal en segundos
frecuencia_muestreo = 500  # Frecuencia de muestreo en Hz

# Creacion de vector de tiempo desde cero a l periodo, con un intervalo Ts
tiempo = np.arange(0, periodo_senoidal, 1 / frecuencia_muestreo)

# Creacion de la señal senoidal
senoidal = amplitud_senoidal * np.sin(2 * np.pi * frecuencia_senoidal * tiempo)

# Figura con la señal continua
plt.figure(figsize=(10, 4))
plt.plot(tiempo, senoidal)
plt.title('Señal Senoidal Continua')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()

# Creacion de vector de muestras discretas a una determinada Fs
muestras = np.arange(0, periodo_senoidal, 1 / frecuencia_muestreo)

# Creacion de la señal senoidal descretizada
senoidal_discretizada = amplitud_senoidal * np.sin(2 * np.pi * frecuencia_senoidal * muestras)

# Figura con la señal discreta
plt.figure(figsize=(10, 4))
plt.stem(muestras, senoidal_discretizada, basefmt=' ')
plt.title('Señal Senoidal Discretizada')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.show()
