# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:29:55 2022

@author: Administrator
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from scipy.spatial import ConvexHull

# Params
T = 5
N = 500000
dt = T / N
sqrtdt = np.sqrt(dt)

# Generate Brownian motion
dW1 = np.random.normal(0, sqrtdt, N)
dW2 = np.random.normal(0, sqrtdt, N)
W1 = dW1.cumsum()
W2 = dW2.cumsum()
W = np.array([W1, W2]).T

# Generate convex hull and reformat W points for ease later
hull = ConvexHull(W)
Wpts = W.reshape(-1, 1, 2)
segments = np.concatenate([Wpts[:-1], Wpts[1:]], axis=1)

# Formatting
plt.style.use("bmh")
fig = plt.figure(figsize = (12, 12), dpi = 350)
ax = fig.add_subplot(111)
ax.set_aspect("equal")

# Colouring/formatting line plot
lc = LineCollection(segments)
lc.set_array(np.linspace(0, 1, N))
lc.set_linewidth(0.5)
line = ax.add_collection(lc)

# Plotting convex hull
hullCoords = list()
for simplex in hull.simplices:
    hullCoords += list(simplex)
    plt.plot(W[simplex, 0], W[simplex, 1], "k", linewidth = 0.8)
plt.fill(W[hull.vertices, 0], W[hull.vertices, 1], "b", alpha = 0.09)

# The BM has already been plotted, this final step is just for axis formatting
plt.plot(W1, W2, alpha = 0)
plt.title("Convex hull of Brownian motion up to time T = 5")
plt.show()

