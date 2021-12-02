#!/bin/python3
"""
    EVSim
    Vehicle.py

    D C Potts 2021
"""

class Vehicle:

    def __init__(self, simParameters, curbMass, powertrain):
        self._simParameters = simParameters

        self._curbMass = curbMass
        self._powertrain = powertrain

        # Sim storage
        self.netForceSeries = simParameters.get1DSeries()
        self.accelSeries = simParameters.get1DSeries()
        self.velocitySeries = simParameters.get1DSeries()
        self.dispSeries = simParameters.get1DSeries()
        return

    def getNetForce(self):
        forceTractive = 1
        forceGravity = 0
        forceAero = 0
        forceRR = 0

        return forceTractive - forceGravity - forceAero - forceRR

    def getMass(self):
        massInertiaWheels = 0
        massInertiaGearbox = 0
        massInertia = massInertiaWheels + massInertiaGearbox
        return self._curbMass + massInertia

    # Simulation step
    def step(self, time, index):
        # Net force
        self.netForceSeries[index] = self.getNetForce()

        # Acceleration
        self.accelSeries[index] = self.netForceSeries[index]/self.getMass()

        # Velocity
        if index == 0:
            self.velocitySeries[index] = 0
        else:
            self.velocitySeries[index] = self.velocitySeries[index - 1] + self.accelSeries[index - 1]*self._simParameters.timeStep

        # Displacement
        if index == 0:
            self.dispSeries[index] = 0
        else:
            self.dispSeries[index] = self.dispSeries[index - 1] + self.velocitySeries[index - 1]*self._simParameters.timeStep
        return
