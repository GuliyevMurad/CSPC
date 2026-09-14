import time
import decay

N0 = 200000
rate = 0.4

# 1. Замер времени для цикла на чистом Python
t0 = time.perf_counter()
res_loop = decay.simulate_loop(N0, rate)
t1 = time.perf_counter()
t_loop = t1 - t0

# 2. Замер времени для векторной версии NumPy
t0 = time.perf_counter()
res_vec = decay.simulate(N0, rate)
t1 = time.perf_counter()
t_numpy = t1 - t0

speedup = t_loop / t_numpy

print(f"Python loop time: {t_loop:.6f} seconds")
print(f"NumPy time:       {t_numpy:.6f} seconds")
print(f"NumPy is {speedup:.2f}x faster")