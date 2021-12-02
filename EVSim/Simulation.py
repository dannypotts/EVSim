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

    def getTimeSeries(self):
        return np.linspace(0, self.maxTime, num = int(self.maxTime/self.timeStep))

    def get1DSeries(self):
        return np.zeros(int(self.maxTime/self.timeStep))

class Simulation:

    def __init__(self, parameters, vehicle):
        self._parameters = parameters
        self._vehicle = vehicle
        return

    def vehicle(self):
        return self._vehicle

    def run(self):
        if self._vehicle is None:
            print("[Simulation.py] No vehicle, cannot run!")
            return

        # Initialise storage
        self.timeSeries = self._parameters.getTimeSeries()

        # Simulate!
        for index, time in enumerate(self.timeSeries):
            self._vehicle.step(time, index)

        return
