import pyNN.brian as sim
import matplotlib.pyplot as plt
import time

def run_sim(ncell):

    print "Cells: ", ncell

    setup0 = time.time()

    sim.setup(timestep=0.025)

    hh_cell_type = sim.HH_cond_exp()

    hh = sim.Population(ncell, hh_cell_type)

    pulse = sim.DCSource(amplitude=0.5, start=20.0, stop=80.0)
    pulse.inject_into(hh)

    hh.record('v')

    setup1 = time.time()

    t0 = time.time()

    sim.run(100.0)

    v = hh.get_data()

    sim.end()

    t1 = time.time()

    setup_total = setup1 - setup0
    run_total = t1 - t0
    print "Setup: ", setup_total
    print "Run: ", run_total
    print "Total sim time: ", setup_total + run_total
    return run_total

times = []
cell_counts = [1, 10, 100, 1000, 2500, 5000, 7500, 10000]

for n in cell_counts:
    times.append(run_sim(n))

plt.plot(cell_counts, times, '-ko')
plt.xlabel("# cells")
plt.ylabel("Simulation time (s)")
plt.title("PyNN using NEURON as simulator")
plt.show()
