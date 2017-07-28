import matplotlib.pyplot as plt

cell_counts = [1, 10, 100, 1000, 2500, 5000, 7500, 10000]

brian1_times = [0.833678007126, 1.41370606422, 1.50416898727, 3.5109500885,
                7.17884778976, 8.04022502899, 17.6114399433, 29.937068224]

brian2_times = [1.08122611046, 0.723483085632, 0.739681005478, 1.15823197365,
                1.81799221039, 2.9335091114, 4.07256388664, 5.15031290054]

nrnpython_times = [0.00740194320679, 0.013386964798, 0.0886888504028, 1.19363594055,
                4.5442340374, 17.884016037, 34.3799350262, 58.1359779835]

pynn_with_neuron_times = [0.0176310539246, 0.0255150794983, 0.158596992493, 1.99696516991,
                        16.2666862011, 64.882158041, 179.34285903, 346.945141077]

pynn_with_brian_times = [3.91313624382, 3.8574860096, 3.94870305061, 5.52180409431,
                        7.90084600449, 11.3757030964, 14.8887498379, 18.3629081249]

neuron_times = [0.02, 0.03, 0.09, 0.86, 2.8, 13.31, 28.26, 49.32]

pynest_times = [0.00632691383362, 0.0424859523773, 0.331573963165, 3.29492783546,
                8.20970392227, 16.3669438362, 24.6245369911, 33.1562879086]

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
plt.title("Simulation time for HH cells with current injection, dt=0.025 ms")
plt.legend()

plt.show()
