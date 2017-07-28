import matplotlib.pyplot as plt

cell_counts = [1, 10, 100, 1000, 2500, 5000, 7500, 10000]

brian1_times = [0.302291154861, 0.379788160324, 0.391832828522, 0.903788089752,
                1.83653998375, 2.0131649971, 4.37163209915, 7.48405313492]

brian2_times = [0.875889062881, 0.597356081009, 0.624230623245, 0.713934898376,
                0.879640102386, 1.18146181107, 1.38487792015, 1.65139698982]

nrnpython_times = [0.00283408164978, 0.00443696975708, 0.0265159606934,
                0.427201032639, 1.3185479641, 4.76109004021, 9.27501296997,
                16.0029139519]

pynn_with_neuron_times = [0.0153019428253, 0.0120878219604, 0.0598411560059,
                0.625998020172, 4.48564004898, 17.0399720669, 48.2111821175,
                100.903879881]

pynn_with_brian_times = [0.678803920746, 0.721149206161, 0.709685087204, 1.00566506386,
                1.56717896461, 2.22348117828, 3.11689376831, 3.84528875351]

neuron_times = [0.01, 0.01, 0.05, 0.33, 1.22, 4.39, 8.76, 15.52]

pynest_times = [0.00351095199585, 0.0101380348206, 0.111765861511, 1.00185108185,
                2.40298509598, 4.93426513672, 7.50378012657, 10.0719850063]

# In order of speed from slowest to fastest
plt.plot(cell_counts, pynn_with_neuron_times, '-o', label='PyNN with NEURON')
plt.plot(cell_counts, nrnpython_times, '-o', label='nrnpython')
plt.plot(cell_counts, neuron_times, '-o', label='NEURON')
plt.plot(cell_counts, brian1_times, '-o', label='Brian1')
plt.plot(cell_counts, pynn_with_brian_times, '-o', label='PyNN with Brian1')
plt.plot(cell_counts, brian2_times, '-o', label='Brian2')
plt.plot(cell_counts, pynest_times, '-o', label='PyNEST')


plt.xlabel("# cells")
plt.ylabel("Simulation time (s)")
plt.title("Simulation time for HH cells with current injection, dt=0.1 ms")
plt.legend()

plt.show()
