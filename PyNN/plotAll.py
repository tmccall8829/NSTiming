import matplotlib.pyplot as plt

cell_counts = [1, 10, 100, 1000, 2500, 5000, 7500, 10000]

brian1_times = [0.302291154861, 0.379788160324, 0.391832828522, 0.903788089752,
                1.83653998375, 2.0131649971, 4.37163209915, 7.48405313492]

brian2_times = [0.875889062881, 0.597356081009, 0.624230623245, 0.713934898376,
                0.879640102386, 1.18146181107, 1.38487792015, 1.65139698982]

nrnpython_times = [0.00740194320679, 0.013386964798, 0.0886888504028, 1.19363594055,
                4.5442340374, 17.884016037, 34.3799350262, 58.1359779835]

pynn_with_neuron_times = [0.0153019428253, 0.0120878219604, 0.0598411560059,
                0.625998020172, 4.48564004898, 17.0399720669, 48.2111821175,
                100.903879881]

pynn_with_brian_times = [0.678803920746, 0.721149206161, 0.709685087204, 1.00566506386,
                1.56717896461, 2.22348117828, 3.11689376831, 3.84528875351]

neuron_times = [0.02, 0.03, 0.09, 0.86, 2.8, 13.31, 28.26, 49.32]

# In order of speed from slowest to fastest
plt.plot(cell_counts, pynn_with_neuron_times, '-o', label='PyNN with NEURON')
plt.plot(cell_counts, nrnpython_times, '-o', label='nrnpython')
plt.plot(cell_counts, neuron_times, '-o', label='NEURON')
plt.plot(cell_counts, brian1_times, '-o', label='Brian1')
plt.plot(cell_counts, pynn_with_brian_times, '-o', label='PyNN with Brian')
plt.plot(cell_counts, brian2_times, '-o', label='Brian2')

plt.xlabel("# cells")
plt.ylabel("Simulation time (s)")
plt.title("Simulation time for HH cells with current injection")
plt.legend()

plt.show()
