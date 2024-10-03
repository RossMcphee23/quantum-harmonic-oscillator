# Basic structure

#Firstly use the easiest method to get the hermite polynomial
import numpy as np

# USE IF STATEMENT TO GENERATE RECURRENCE RELATION
def hermite_polynomial(n,x):
    if n ==0:
        return np.ones_like(x) # creates an array of 1's
    elif n ==1:
        return 2*x
    else:
        return 2*x*hermite_polynomial(n-1,x) - 2 * (n-1)*hermite_polynomial(n-2,x)
    