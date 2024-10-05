# Imports needed, note that wavefunction using hermite from 'hermite.py'

import numpy as np
import matplotlib as plt
from wavefunction import wavefunction

def plot_wavefunctions(max_n, x_vals):
    plt.figure(figsize=(12, 8))
    for n in range(max_n + 1):
        psi_n = wavefunction(n, x_vals)
        plt.plot(x_vals, psi_n, label=f'n={n}')
    plt.title('Harmonic Oscillator Wavefunctions')
    plt.xlabel('x')
    plt.ylabel('$\psi_n(x)$')
    plt.legend()
    plt.grid()
    plt.show()

    