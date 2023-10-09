# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 14:08:32 2023

@author: talbanesi
"""

import numpy as np
import matplotlib.pyplot as plt

# Señal continua en el tiempo

fs = 100000 # En Hz

amplitud = 10 # En unidades de amplitud de señal (Ej. V, A, etc)
frecuencia = 500 # Frecuencia en Hz de la señal

# duracion = 0.1 # Duracion de la señal en segundos

periodos = 2 # Cantidad de periodos a contemplar
duracion = periodos * (1/frecuencia)

# Creacion de vector de tiempo
tiempo_continuo = np.linspace(0, duracion, int(duracion * fs), endpoint=False)  

# Crear la señal continua (en este caso, una señal sinusoidal)
señal_continua = amplitud * np.sin(2 * np.pi * frecuencia * tiempo_continuo)

# Crear un arreglo de tiempo para la señal discreta
tiempo_discreto = np.arange(0, duracion, 1 / fs)

# Muestrear la señal continua para obtener la señal discreta
señal_discreta = amplitud * np.sin(2 * np.pi * frecuencia * tiempo_discreto)

# Graficar la señal continua
plt.figure(figsize=(12, 4))
plt.subplot(2, 1, 1)
plt.plot(tiempo_continuo, señal_continua)
plt.title('Señal Continua')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

plt.subplot(2, 1, 2)
plt.stem(tiempo_discreto, señal_discreta, markerfmt='ro', basefmt='r', linefmt='r-')
plt.title('Señal Discreta (muestreada)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.tight_layout()