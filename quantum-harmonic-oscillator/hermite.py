# Basic structure

#Firstly use the first know coefficients from theory
import numpy as np

def hermite_polynomial(n,x):
    H_0 = np.ones_like(x)
    if n == 0:
        return H_0
    H_1 = 2 * x
    if n == 1:
        return H_1
    
    
    # Need iterative scheme for higher orders: Use if statement
    Hn_minus_2 = H_0
    Hn_minus_1 = H_1

    for i in range(2, n+1):
        H_n = 2 * x * Hn_minus_1 - 2 * (i - 1) * Hn_minus_2
        Hn_minus_2, Hn_minus_1 = Hn_minus_1, H_n #Updates Hn-2 to Hn-1 and Hn-1 to Hn simultaneously

    return H_n

