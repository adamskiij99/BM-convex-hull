#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:03:55 2022

@author: jonesac
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# Create a planar BM
def BM(rho):
    dW1 = np.random.normal(0, sqrtdt, N)
    dW2 = rho * dW1 + np.sqrt(1 - rho * rho) * np.random.normal(0, sqrtdt, N)
    W1 = dW1.cumsum()
    W2 = dW2.cumsum()
    W = np.array([W1, W2]).T
    return W

# Params
T = 1
N = 5000
dt = T / N
sqrtdt = np.sqrt(dt)
rho = 0     # Correlation parameter (NB: doesn't work for 1 or -1; degenerate hull)
m = 50000   # For Monte Carlo

# Initialise
P = list()
A = list()

# Monte Carlo
for i in range(m):
    # Generate Brownian motion
    W = BM(rho)
    # Initialise perims and areas
    p = list()
    a = list()
    # Create convex hull of the BM
    hull = ConvexHull(W)
    # then add its perimeter (hull.area) and area (hull.volume) to P, A
    p += [hull.area]
    a += [hull.volume]
    P += [p]
    A += [a]
P = np.array(P).T
A = np.array(A).T

# Plotting
plt.style.use("bmh")
fig, ax = plt.subplots(1, 1, figsize = (10, 6))
ax.set_title("Perim and area distns of conv hull of BM to time T=1")
ax.hist(P[0], bins = 100, density = True, label = "Perim")
ax.hist(A[0], bins = 100, density = True, label = "Area")
plt.legend()
plt.show()


