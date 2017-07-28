from neuron import h, gui
import matplotlib.pyplot as plt
import time
from hhType import HHCell
import numpy as np


def run_sim(ncell):
    print "Cells: ", ncell

    setup0 = time.time()

    cells = []

    i = 0

    while i <= ncell - 1:
        cell = HHCell()
        cells.append(cell)
        i += 1

    h.tstop = 100.0
    h.dt = 0.1
    h.steps_per_ms = 10

    setup1 = time.time()

    t0 = time.time()

    h.run()

    t1 = time.time()

    setup_total = setup1 - setup0
    run_total = t1 - t0
    print "Setup: ", setup_total
    print "Run: ", run_total
    print "Total sim time: ", setup_total + run_total

    return run_total


cell_counts = [1, 10, 100, 1000, 2500, 5000, 7500, 10000]
times = [run_sim(n) for n in cell_counts]

np.savetxt("nrnpythontdata.txt", times, newline="\n")

# plt.plot(cell_counts, times, '-ko')
# plt.xlabel("# cells")
# plt.ylabel("Simulation time (s)")
# plt.title("nrnpython times")
# plt.show()
