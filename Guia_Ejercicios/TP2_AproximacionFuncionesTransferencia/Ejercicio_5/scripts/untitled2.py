# -*- coding: utf-8 -*-
"""
Created on Thu May 11 10:46:26 2023

@author: talbanesi
"""

import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
# from splane import analyze_sys # version vieja
from pytc2.sistemas_lineales import analyze_sys

# # Definicion de la funcion transferencia
# orden = 5

# z,p,k = sig.cheb1ap(orden, 0.4)

# print("Las raices del filtro son: ")
# print

# my_tf1 = sig.TransferFunction([1,0], [1,2.59])
# my_tf2 = sig.TransferFunction([1,0,0], [1,0.226,0.952])
# my_tf3 = sig.TransferFunction([1,0,0], [1,1.27,2.02])

# num1, den1 = my_tf1.num, my_tf1.den
# num2, den2 = my_tf2.num, my_tf2.den
# num3, den3 = my_tf3.num, my_tf3.den

# num = sig.convolve(sig.convolve(num1, num2), num3)
# den = sig.convolve(sig.convolve(den1, den2), den3)
# H = sig.TransferFunction(num, den)

# analyze_sys(H)

plt.close("all")

my_tf1 = sig.TransferFunction([1,0,0], [1,1.8477,1])
my_tf2 = sig.TransferFunction([1,0,0], [1,0.7653,1])

num1, den1 = my_tf1.num, my_tf1.den
num2, den2 = my_tf2.num, my_tf2.den

num = sig.convolve(num1, num2)
den = sig.convolve(den1, den2)
H = sig.TransferFunction(num, den)

analyze_sys(H)