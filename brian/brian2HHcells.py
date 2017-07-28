from brian2 import *
import matplotlib.pyplot as plt
import time

def run_sim(ncell):
    print "Cells: ", ncell
    defaultclock.dt = 0.025 * ms

    setup0 = time.time()

    El = 10.6 * mV
    gl = 0.3 * msiemens
    eqs_leak = Equations('I_leak = gl * (El - vm) : amp')


    EK = -12 * mV
    gK = 36 * msiemens
    eqs_K = Equations('''I_K = gK * n**4 * (EK - vm) : amp
                     dn/dt = alphan * (1 - n) - betan * n : 1
                     alphan = 0.01 * (10 * mV - vm) / (exp(1 - 0.1 * vm / mV) - 1) / mV / ms : Hz
                     betan = 0.125 * exp(-0.0125 * vm / mV) / ms : Hz''')

    ENa = 120 * mV
    gNa = 120 * msiemens
    eqs_Na = Equations('''I_Na = gNa * m**3 * h * (ENa - vm) : amp
                      dm/dt = alpham * (1 - m) - betam * m : 1
                      dh/dt = alphah * (1 - h) - betah * h : 1
                      alpham = 0.1 * (25 * mV - vm)/(exp(2.5 - 0.1 * vm / mV) - 1) / mV / ms : Hz
                      betam = 4 * exp(-0.0556 * vm / mV) / ms : Hz
                      alphah = 0.07 * exp(-0.05 * vm / mV) / ms : Hz
                      betah = 1.0 / (1 + exp(3.0 - 0.1 * vm / mV)) / ms : Hz''')

    C = 1 * uF

    eqs = Equations('''dvm/dt = (I_leak + I_K + I_Na + I_inj) / C : volt
                       I_inj : amp''') + eqs_leak + eqs_K + eqs_Na

    neuron = NeuronGroup(ncell, eqs, method='exponential_euler')

    neuron.I_inj = 0 * uA
    M = StateMonitor(neuron, 'vm', record=True)

    setup1 = time.time()

    t0 = time.time()

    run(20 * ms)
    neuron.I_inj = 40 * uA
    run(60 * ms)
    neuron.I_inj = 0 * uA
    run(20 * ms)

    t1 = time.time()
    setup_total = setup1 - setup0
    run_total = t1 - t0
    print "Setup: ", setup_total
    print "Run: ", run_total
    print "Total sim time: ", setup_total + run_total

    # plt.plot(M.t / ms, M[0].vm / mV)
    # plt.show()

    return run_total

times = []
cell_counts = [1, 10, 100, 1000, 2500, 5000, 7500, 10000]
for celln in cell_counts:
    times.append(run_sim(celln))

plt.plot(cell_counts, times, '-ko')
plt.xlabel("# cells")
plt.ylabel("Simulation time (s)")
plt.title("Brian2")
plt.show()
