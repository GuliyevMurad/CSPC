"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result:
#   (1) gradient descent by hand (loop x = x - lr*df(x) until the step is tiny)
x = 0.0
lr = 0.1
for _ in range(1000):
    step = lr * df(x)
    x -= step
    if abs(step) < 1e-7:
        break
print("2A Gradient descent:", x)

#   (2) scipy.optimize.newton(df, x0, fprime=d2f)
res_newton_2a = newton(df, 0.0, fprime=d2f)
print("2A Newton:", res_newton_2a)

#   (3) scipy.optimize.minimize(f, x0, method="SLSQP")
res_slsqp_2a = minimize(f, 0.0, method="SLSQP")
print("2A SLSQP:", res_slsqp_2a.x[0])


# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
print("\n2B Results:")
for x0 in [0.0, 2.0]:
    print(f"\nStarting from x0 = {x0}:")
    
    # (1) Gradient descent by hand
    x = x0
    for _ in range(10000):
        step = 0.01 * dg(x)
        x -= step
        if abs(step) < 1e-8:
            break
    print(f"  Gradient descent: x = {x:.4f}, g(x) = {g(x):.4f}")
    
    # (2) Newton
    try:
        n_res = newton(dg, x0, fprime=d2g)
        curvature = d2g(n_res)
        print(f"  Newton: x = {n_res:.4f}, g''(x) = {curvature:.2f} ({'minimum' if curvature > 0 else 'maximum'})")
    except Exception as e:
        print(f"  Newton failed: {e}")
        
    # (3) SLSQP
    s_res = minimize(g, x0, method="SLSQP")
    print(f"  SLSQP: x = {s_res.x[0]:.4f}, g(x) = {g(s_res.x[0]):.4f}")