## About
This repository contains files for testing the simulation speeds of the following neural simulators:
- PyNN (using NEURON, Brian1, and NEST)
- NEURON
- Neuron + python (nrnpython)
- Brian1
- Brian2
- NEST

More simulators and languages will likely be added over time. Below is a link to a google drive document containing the most up-to-date tables and graphs.

https://docs.google.com/document/d/15IH_tMI8lW55fWY-5HKK71PTs1TTPU3ohYhZSScKvqc/edit?usp=sharing

## Methods
To test the simulation speed of the different simulators, we create networks of simple Hodgkin-Huxley cells with constant current injections. At the moment, the simulators create 1, 10, 100, 1000, 2500, 5000, 7500, and 10000 cells and run the simulation for t=100 ms. The cell numbers may change over time.
