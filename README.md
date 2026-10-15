# CSPC Computer Science for Physics and Chemistry

## PW1
**Lab A: Reproducible Foundations**

**What I built:**
Built the foundational CSPC repository with a configured Conda environment, wrote unit tests using pytest, and created a script to compare computation performance.

**Speed comparison (loop vs NumPy):**
loop : 2.839364 s
numpy : 0.000291 s
speed-up: ~9768 faster

**Tests:** all passing? 
yes

**Conclusion:**
Using NumPy is much faster than standard Python loops for large physics simulations, and the Conda/pytest setup makes sure the working environment is stable and easy to reproduce. Note: I used an AI assistant as a tutor to help me understand the code and guide me through the necessary terminal commands.



**Lab B: Radioactive Decay & Snakemake Automation**

**What I built:**
Visualized experimental radioactive decay data from a CSV file and compared it against the theoretical analytical decay law using a 1x2 matplotlib subplot with shared axes, also and automated the whole workflow using a Snakemake pipeline.

**Data & Results:**
Initial Count (N0): 5000 at t = 0.0 s
Decay Constant: 0.3
Observation: The observed points follow the theoretical decay line well, showing only small, expected ups and downs.

**Automation:**
The Snakemake rule automatically tracks dependencies between decay_observed.csv, plot.py, and figure.png, recompiling the chart only when inputs change or the output is missing.

**Conclusion:**
Using Python and Snakemake together makes data analysis easy to repeat and saves time by avoiding doing the same work twice. Note: I used an AI assistant as a tutor to help me understand the code and guide me through the terminal commands.








## PW2
**Lab A: Motion from Tracking Data**

Why acceleration is noisy: Taking two derivatives magnifies tiny measurement errors from the position data, making the acceleration look very rough.

**What I built:** 
Processed noisy free-fall position measurements by taking numerical derivatives using NumPy to compute velocity and acceleration, and then used cumulative trapezoidal integration to recover the original position.

**Data & Results:** 
- Mean acceleration: -8.58 m/s² (close to the true free-fall value of -9.81 m/s²).
- Standard deviation of acceleration: 28.72 (showing high noise).
- Max difference after integrating back: ~0.78 meters.

**Conclusion:**
Differentiation amplifies noise while integration cleans it up, which is an important lesson for handling real data. Note: I used an AI assistant as a tutor to help me understand the code and guide me through the terminal commands.



**Lab B: Optimization in Chemistry**

**What I built:** Compared three optimization methods (gradient descent, Newton's method, and SLSQP) on convex and complex functions, and then applied optimization techniques to fit a first-order reaction rate constant, solve a chemical equilibrium problem and locate a titration equivalence point.

**Data & Results:** 
- **Warm-up (Part 2):**
On the easy function, all three methods reached x ≈ 3. On the harder landscape, the starting point changed the final result, and Newton's method from x0 = 0 landed on a maximum (g''(x) = -5.65) rather than a minimum because it only finds where the slope is zero.

- **Kinetics (Part 3):** 
Fitted the rate constant k ≈ 0.26 for the decaying concentration data.

- **Equilibrium (Part 4):** 
Both Newton and SLSQP converged to the extent x ≈ 0.66, giving equilibrium amounts of H2 = 0.34 mol, I2 = 0.34 mol, and HI = 1.33 mol.

- **Titration (Part 5):** 
Located the titration equivalence point at exactly 50.00 mL using numerical differentiation (`np.gradient`).

**Conclusion:** 
Optimization methods behave differently depending on the starting point and the algorithm used and techniques like minimization and root-finding are powerful tools for solving real chemistry problems. Note: I used an AI assistant as a tutor to help me understand the code and guide me through the terminal commands.
