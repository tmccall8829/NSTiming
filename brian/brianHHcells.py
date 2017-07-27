from brian import *
from brian.library.ionic_currents import *
import matplotlib.pyplot as plt
import time

def run_sim(ncell):
    print "Cells: ", ncell

    setup0 = time.time()

    El = 10.6 * mV
    EK = -12 * mV
    ENa = 120 * mV
    eqs = MembraneEquation(1 * uF) + leak_current(.3 * msiemens, El)
    eqs += K_current_HH(36 * msiemens, EK) + Na_current_HH(120 * msiemens, ENa)
    eqs += Current('I:amp')

    neuron = NeuronGroup(ncell, eqs, implicit=True, freeze=True)
    neuron.I = 0 * uA
    trace = StateMonitor(neuron, 'vm', record=True)

    setup1 = time.time()

    t0 = time.time()

    run(20 * ms)
    neuron.I = 40 * uA
    run(60 * ms)
    neuron.I = 0 * uA
    run(20 * ms)

    t1 = time.time()
    setup_total = setup1 - setup0
    run_total = t1 - t0
    print "Setup: ", setup_total
    print "Run: ", run_total
    print "Total sim time: ", setup_total + run_total
    return run_total

    #plt.plot(trace.times / ms, trace[0] / mV)
    #plt.show()

times = []
cell_counts = [1, 10, 100, 1000, 2500, 5000, 7500, 10000]
for celln in cell_counts:
    times.append(run_sim(celln))

plt.plot(cell_counts, times, '-ko')
plt.xlabel("# cells")
plt.ylabel("Simulation time (s)")
plt.title("Brian")
plt.show()
