# Here we define the wave function, normalisation and more

from hermite import hermite_polynomial
import numpy as np

def wavefunction(n,x):
    #Need to recognize normalisation to keep area = 1
    norm = 1/(2**n * np.factorial(n) * np.sqrt(np.pi)) 
    #Now simply calculate wavefunction using definition
    psi_n = norm * hermite_polynomial(n,x) * np.exp(-x**2/2) #importing from hermite.py
    return psi_n

# with the info we have, we can calculate expectation values

def expectation_value(n, x_vals):
    psi_n = wavefunction(n,x_vals)
    prob_density = np.abs(psi_n)**2
    expectation_value = np.trapz(x_vals*prob_density, x_vals)
    expectation_value2 = np.trapz(x_vals**2 * prob_density, x_vals)
    std_deviation = np.sqrt(expectation_value2 - expectation_value**2)
    return expectation_value, std_deviation

# we also know that there is a momentum 'wavefunction' representation

#phi(k) = 1/sqrt(2pihbar) I(psi(x)*exp(-ipx/hbar)dx, so we need to use a fft 
def momentum_wavefunction(n, p_vals):
    # Generate a range of x values
    x_vals = np.linspace(-10, 10, 500)
    psi_n_x = wavefunction(n, x_vals)
    
    # Fourier transform to momentum space
    psi_n_p = np.fft.fftshift(np.fft.fft(psi_n_x))
    p_space = np.fft.fftshift(np.fft.fftfreq(x_vals.size, d=(x_vals[1] - x_vals[0])))
    
    # Interpolate the result to match p_vals
    return np.interp(p_vals, p_space, np.abs(psi_n_p))

def momentum_expectation_value(n, p_vals):
    psi_n_p = momentum_wavefunction(n, p_vals)
    probability_density_p = np.abs(psi_n_p)**2
    expectation_p = np.trapz(p_vals * probability_density_p, p_vals)
    expectation_p2 = np.trapz(p_vals**2 * probability_density_p, p_vals)
    uncertainty_p = np.sqrt(expectation_p2 - expectation_p**2)
    return expectation_p, uncertainty_p

def calculate_energy(n):
    # For the quantum harmonic oscillator, the energy levels are given by E_n = (n + 1/2) * ħω
    # Assuming ħω = 1 for simplicity
    energy_n = (n + 0.5)
    return energy_n

# Require time evolving wavefunction for simulation
def wavefunction_t(n, x_vals, t, omega = 1.0):
    psi_n = wavefunction(n,t)
    E = calculate_energy(n)
    time_factor = np.exp(-1j * E * omega * t)
    return psi_n * time_factor