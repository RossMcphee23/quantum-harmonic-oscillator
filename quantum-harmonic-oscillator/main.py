# Main program with user interaction
import numpy as np 
from wavefunction import expectation_value, momentum_expectation_value, uncertainty_p, uncertainty_x
from visualization import plot_wavefunctions


def main():
    x_vals = np.linspace(-5, 5, 500)
    max_n = int(input("Enter the maximum quantum number to plot (e.g., 3): "))
    plot_wavefunctions(max_n, x_vals)
    
    n = int(input("Enter a quantum number to calculate expectation values (e.g., 1): "))
    expectation_x, uncertainty_x = (n, x_vals)
    print(f'Expectation value <x>: {expectation_x}')
    print(f'Uncertainty in x: {uncertainty_x}')

if __name__ == "__main__":
    main()
