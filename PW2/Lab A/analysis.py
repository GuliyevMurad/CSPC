"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
- differentiate once  -> velocity
- differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
- integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
data = np.loadtxt('freefall.csv', delimiter=',', skiprows=1)
t = data[:, 0]
y = data[:, 1]

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y, t)
a = np.gradient(v, t)

print("Mean acceleration:", a.mean())
print("Acceleration std dev:", a.std())

# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

diff = np.max(np.abs(y - y_rec))
print("Max difference:", diff)

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig, ax = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

ax[0].plot(t, y)
ax[0].set_ylabel('y')

ax[1].plot(t, v)
ax[1].set_ylabel('v')

ax[2].plot(t, a)
ax[2].axhline(-9.81, color='r', linestyle='--')
ax[2].set_xlabel('t')
ax[2].set_ylabel('a')

plt.tight_layout()
plt.savefig('motion.png')