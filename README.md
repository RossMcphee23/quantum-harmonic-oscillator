# Quantum Harmonic Oscillator

This project provides a numerical and visual exploration of the quantum 
harmonic oscillator using Hermite polynomials. It includes functions to 
generate Hermite polynomials, calculate wavefunctions for different quantum 
states, and visualize the probability densities of these wavefunctions. 
Additionally, it computes physical properties such as expectation values 
and uncertainties, offering insights into the quantum harmonic oscillator 
system.

## Features
- **Hermite Polynomial Generation:** Uses the recurrence relation:
  \[
  H_{n+1}(x) = 2xH_n(x) - 2nH_{n-1}(x)
  \]
  to generate Hermite polynomials up to an arbitrary order.
- **Wavefunction Calculation:** Computes the wavefunctions of the harmonic 
oscillator:
  \[
  \psi_n(x) = N_n H_n(x) e^{-\frac{x^2}{2}}
  \]
  where \( H_n(x) \) is the Hermite polynomial, and \( N_n \) is the 
normalization factor.
- **Expectation Value Computation:** Calculates the expectation values of 
position (\( \langle x \rangle \)) and uncertainty (\( \Delta x \)):
  \[
  \langle x \rangle = \int_{-\infty}^{\infty} x |\psi_n(x)|^2 \, dx
  \]
  \[
  \Delta x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2}
  \]
- **Visualization:** Plots wavefunctions and probability densities for 
different quantum states.

## Installation

To run this project, ensure you have Python 3.x and the necessary 
dependencies installed:

1. Clone the repository:
   ```bash
   git clone 
https://github.com/RossMcphee23/quantum-harmonic-oscillator.git


