#!/bin/python3
"""
    EVSim
    plot_functions.py

    D C Potts 2021
"""

import matplotlib.pyplot as plt

def plotSimulation(simulation):
    # Net force
    plt.subplot(2, 2, 1)
    plt.plot(simulation.timeSeries, simulation.vehicle().netForceSeries)
    plt.xlabel("Time (s)")
    plt.ylabel("Net Tractive Force (N)")
    plt.grid(visible = True, which = 'both')

    # Acceleration
    plt.subplot(2, 2, 2)
    plt.plot(simulation.timeSeries, simulation.vehicle().accelSeries)
    plt.xlabel("Time (s)")
    plt.ylabel("Acceleration (m/s^2)")
    plt.grid(visible = True, which = 'both')

    # Velocity
    plt.subplot(2, 2, 3)
    plt.plot(simulation.timeSeries, simulation.vehicle().velocitySeries)
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.grid(visible = True, which = 'both')

    # Displacement
    plt.subplot(2, 2, 4)
    plt.plot(simulation.timeSeries, simulation.vehicle().dispSeries)
    plt.xlabel("Time (s)")
    plt.ylabel("Displacement (m)")
    plt.grid(visible = True, which = 'both')

    plt.tight_layout()
    plt.show()
    return
