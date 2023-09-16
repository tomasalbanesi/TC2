# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 12:08:35 2023

@title: TP5 Filtros digitales ejercicio 2)a)
@filename: Script_TP5_Ejercicio2A.py
@author: Tomas Agustin Albanesi
"""

# Importacion de modulos y funciones
import matplotlib.pyplot as plt
import scipy.signal as signal
import numpy as np
from pytc2.sistemas_lineales import pzmap

# Define los coeficientes del numerador y denominador
numerator = [0.8,  0.0,  1.0]
denominator = [1.0,  0.0,  0.8]

# Crear una representación en espacio de estados
A, B, C, D = signal.tf2ss(numerator, denominator)

# Calcular los polos y ceros
poles = np.linalg.eigvals(A)
zeros = np.roots(numerator)

# Crear puntos en la circunferencia unitaria
theta = np.linspace(0, 2 * np.pi, 100)
circunferencia_unitaria = np.exp(1j * theta)

# Graficar el diagrama de polos y ceros
plt.figure(figsize=[10, 10])
plt.scatter(np.real(poles), np.imag(poles), marker='x', color='r', label='Polos')
plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='b', label='Ceros')
plt.plot(np.real(circunferencia_unitaria), np.imag(circunferencia_unitaria), 'g--', label='Circunferencia Unitaria')
plt.axhline(0, color='k', linestyle='--', linewidth=0.5)
plt.axvline(0, color='k', linestyle='--', linewidth=0.5)
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginaria')
plt.title('Diagrama de Polos y Ceros con Circunferencia Unitaria')
plt.grid()
plt.legend()
plt.axis('equal')  # Asegura que los ejes tengan la misma escala
plt.show()

print('Polos: ')
print(poles)

print('Ceros: ')
print(zeros)

# Calculo la respuesta de frecuencia en el dominio Z
fs = 1
w, h = signal.freqz(numerator, denominator)

# Calculo la magnitud, fase y retardo de grupo
mag = np.abs(h)

phase = np.angle(h)

ejeMuestras = w * (2*np.pi/fs)
group_delay = -np.diff(phase) / np.diff(ejeMuestras)

plt.figure(figsize=(12, 4))
plt.semilogx(w, 20 * np.log10(mag))
plt.title('Respuesta de magnitud')
plt.xlabel('Frecuencia discreta [Hz]')
plt.ylabel('Magnitud [dB]')
plt.ylim([-0.1,0.1])
plt.grid()
plt.show()

plt.figure(figsize=(12, 4))
plt.semilogx(w, np.degrees(phase))
plt.title('Respuesta de fase')
plt.xlabel('Frecuencia discreta [Hz]')
plt.ylabel('Fase [grados]')
plt.ylim([-180,180])
plt.grid()
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 4))
plt.semilogx(w[:-1], group_delay)
plt.title('Retardo de grupo')
plt.xlabel('Frecuencia discreta [Hz]')
plt.ylabel('Retardo de grupo [muestras]')
plt.ylim([-5,5])
plt.grid()
plt.tight_layout()
plt.show()