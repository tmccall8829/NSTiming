import nest
import matplotlib.pyplot as plt
import time

"""
Note: default units in nest
time - ms
voltage - mV
capacitance - pF
current - pA
conductance - nS
Spike rates in (eg poisson_generator) - spikes/s
modulation frequencies (eg ac_generator) - Hz
"""

def run_sim(ncell):
    print("Cells: ", ncell)

    nest.ResetKernel()

    setup0 = time.time()

    nest.SetKernelStatus({"resolution": 0.025}) # Default is 0.1

    pulse_params = {
    "amplitude": 400.0,
    "start": 20.0,
    "stop": 80.0
    }

    multimeter_params = {
    "withtime": True,
    "record_from": ["V_m"]
    }

    npop        = nest.Create("hh_cond_exp_traub", n=ncell)
    pulse       = nest.Create("dc_generator", params=pulse_params)
    multimeter  = nest.Create("multimeter", params=multimeter_params)

    nest.Connect(pulse, npop)
    nest.Connect(multimeter, npop)

    setup1 = time.time()

    t0 = time.time()

    nest.Simulate(100.0)

    dmm = nest.GetStatus(multimeter)[0] # Get V_m data for cell 0
    Vms = dmm["events"]["V_m"]
    ts = dmm["events"]["times"]

    t1 = time.time()

    # pylab.figure(1)
    # pylab.plot(ts, Vms)
    # pylab.show()
    print("Setup time: ", setup1 - setup0)
    print("Run time: ", t1 - t0)
    print("Total sim time: ", (setup1 - setup0) + (t1 - t0))
    return (setup1 - setup0) + (t1 - t0)

times = []
cell_counts = [1, 10, 100, 1000, 2500, 5000, 7500, 10000]
for celln in cell_counts:
    times.append(run_sim(celln))

plt.plot(cell_counts, times, '-ko')
plt.xlabel("# cells")
plt.ylabel("Simulation time (s)")
plt.title("NEST")
plt.show()
