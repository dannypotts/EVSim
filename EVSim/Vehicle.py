#!/bin/python3
"""
    EVSim
    Vehicle.py

    D C Potts 2021
"""

import pint
uref = pint.UnitRegistry()

class Vehicle:

    def __init__(self, simParameters):
        self._simParameters = simParameters

        self.netForce = simParameters.get1DSeries()
        return

    def setPowertrain(self, powertrain):
        self._powertrain = powertrain
        return

    def getNetForce(self):
        return 1
