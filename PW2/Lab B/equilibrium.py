"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = 1.0  # initial H2
b = 1.0  # initial I2

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
def k_imbalance(x):
    return (2 * x)**2 / ((a - x) * (b - x)) - K

# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
x_newton = newton(k_imbalance, x0=0.5)
print("Extent x (Newton):", x_newton)

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
def objective(x):
    return k_imbalance(x[0])**2

res = minimize(objective, x0=[0.5], method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res.x[0]
print("Extent x (SLSQP):", x_slsqp)

# Equilibrium amounts
h2_eq = a - x_newton
i2_eq = b - x_newton
hi_eq = 2 * x_newton
print(f"Equilibrium amounts -> H2: {h2_eq:.3f}, I2: {i2_eq:.3f}, HI: {hi_eq:.3f}")

# TODO 4: report the equilibrium amounts, and plot how the three
#         amounts change with the extent x, marking the equilibrium.
x_vals = np.linspace(0, 0.95, 200)
h2_vals = a - x_vals
i2_vals = b - x_vals
hi_vals = 2 * x_vals

plt.figure(figsize=(7, 5))
plt.plot(x_vals, h2_vals, label='H2', color='blue')
plt.plot(x_vals, i2_vals, label='I2', color='green')
plt.plot(x_vals, hi_vals, label='HI', color='orange')
plt.axvline(x_newton, color='red', linestyle='--', label=f'Equilibrium x={x_newton:.3f}')
plt.xlabel('Extent of reaction (x)')
plt.ylabel('Moles')
plt.title('Chemical Equilibrium H2 + I2 <=> 2 HI')
plt.legend()
plt.grid(True)
plt.savefig('equilibrium.png')
print("Saved equilibrium.png")