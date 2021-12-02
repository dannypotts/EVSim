#!/bin/python3
"""
    EVSim
    main.py

    D C Potts 2021
"""

from EVSim.Simulation import Simulation, SimulationParameters
from EVSim.Vehicle import Vehicle
from EVSim.Powertrain import Powertrain

from plot_functions import plotSimulation

# Simulation globals
SIM_TIME_STEP = 0.001           # seconds
SIM_MAX_TIME = 30               # seconds

# Vehicle Constants
CAR_CURB_MASS = 1               # kg, not including battery mass

# Powertrain constants
PT_GEAR_RATIO = 12/1

if __name__ == "__main__":
    print("EVSim")

    parameters = SimulationParameters(SIM_TIME_STEP, SIM_MAX_TIME)

    powertrain = Powertrain(PT_GEAR_RATIO)

    car = Vehicle(parameters, CAR_CURB_MASS, powertrain)

    sim = Simulation(parameters, car)
    sim.run()
    plotSimulation(sim)
