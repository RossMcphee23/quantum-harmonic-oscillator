# Here we define the wave function, normalisation and more

from hermite import hermite_polynomial
import numpy as np

def wavefunction(n,x):
    #Need to recognize normalisation to keep area = 1
    norm = 1/(2**n * np.factorial(n) * np.sqrt(np.pi)) 
    #Now simply calculate wavefunction using definition
    psi_n = norm * hermite_polynomial(n,x) * np.exp(-x**2/2) #importing from hermite.py
    return psi_n

# with the info we have, we can calculate expectation values.
# exp value = integral(psistar * x * psi) which is easy since x only acts as x ->

def expectation_value(n, x_vals):
    psi_n = wavefunction(n,x_vals)
    prob_density = np.abs(psi_n)**2
    expectation_value = np.trapz(x_vals*prob_density, x_vals)
    expectation_value2 = np.trapz(x_vals**2 * prob_density, x_vals)
    std_deviation = np.sqrt(expectation_value2 - expectation_value**2)
    return expectation_value, std_deviation
