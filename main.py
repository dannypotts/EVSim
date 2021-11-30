#!/bin/python3
"""
    EVSim
    main.py

    D C Potts 2021
"""

from EVSim.Simulation import Simulation, SimulationParameters
from EVSim.Vehicle import Vehicle

# Simulation globals
SIM_TIME_STEP = 0.001           # seconds
SIM_MAX_TIME = 30               # seconds

if __name__ == "__main__":
    print("EVSim")

    parameters = SimulationParameters(SIM_TIME_STEP, SIM_MAX_TIME)

    car = Vehicle(parameters)

    sim = Simulation(parameters, car)
    sim.run()
