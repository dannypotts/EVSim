#!/bin/python3
"""
    EVSim
    Simulation.py

    D C Potts 2021
"""

import numpy as np

class SimulationParameters:

    def __init__(self, timeStep, maxTime):
        self.timeStep = timeStep
        self.maxTime = maxTime
        return

    def get1DSeries(self):
        return np.zeros(int(self.maxTime/self.timeStep))

class Simulation:

    def __init__(self, parameters, vehicle):
        self._parameters = parameters
        self._vehicle = vehicle

        self.timeSeries = parameters.get1DSeries()
        return

    def run(self):
        if self._vehicle is None:
            print("[Simulation.py] No vehicle, cannot run!")
            return
        return
