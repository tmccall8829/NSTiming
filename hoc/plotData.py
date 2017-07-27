import matplotlib.pyplot as plt

times = [0.02, 0.03, 0.09, 0.86, 2.8, 13.31, 28.26, 49.32]
cell_counts = [1, 10, 100, 1000, 2500, 5000, 7500, 10000]

plt.plot(cell_counts, times, '-ko')
plt.xlabel("# cells")
plt.ylabel("Simulation time (s)")
plt.title("NEURON")
plt.show()
