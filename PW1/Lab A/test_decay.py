"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
def test_rejects_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.4)



# TODO 2: test_matches_law
def test_matches_law():
    N0 = 1000
    decay_rate = 0.4
    t = 1.0
    theoretical_val = N0 * np.exp(-decay_rate * t)

    step_index = 20  
    runs = [simulate(N0, decay_rate)[step_index] for _ in range(100)]
    avg_val = np.mean(runs)

    assert avg_val == pytest.approx(theoretical_val, rel=1e-1)