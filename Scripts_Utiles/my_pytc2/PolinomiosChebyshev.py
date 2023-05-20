import sympy as sp
import pytc2.general as tc2general

# Laplace complex variable. s = σ + j.ω
s = sp.symbols('s', complex=True)
# Fourier real variable ω 
w = sp.symbols('w', complex=False)

def polinomiosChebyshev(n):
    
    Cn_aa = 1
    Cn_a = w
    
    if n > 1:
        
        for i in range(n-1):
            
            Cn = 2 * w * Cn_a - Cn_aa
    
            Cn_aa = Cn_a
            Cn_a = Cn

    elif n == 1:
        
        Cn = Cn_a
        
    else:
        
        Cn = 1
            
    # Retorna polinomio agrupado
    return(sp.expand(Cn))

    # Retorna polinomio simplificado pero separado
    # return(sp.simplify(Cn))

print(polinomiosChebyshev(3))

print(tc2general.Chebyshev_polynomials(3))
