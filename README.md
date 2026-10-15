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

