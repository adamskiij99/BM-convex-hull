# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 15:49:50 2022

@author: Administrator
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.collections import LineCollection
from scipy.spatial import ConvexHull

# Params
T = 2
N = 20000
dt = T / N
sqrtdt = np.sqrt(dt)

# Generate Brownian motion
dW1 = np.random.normal(0, sqrtdt, N)
dW2 = np.random.normal(0, sqrtdt, N)
W1 = dW1.cumsum()
W2 = dW2.cumsum()
W = np.array([W1, W2]).T
Wpts = W.reshape(-1, 1, 2)
segments = np.concatenate([Wpts[:-1], Wpts[1:]], axis=1)
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 15:49:50 2022

@author: Administrator
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.collections import LineCollection
from scipy.spatial import ConvexHull

# Params
T = 2
N = 20000
dt = T / N
sqrtdt = np.sqrt(dt)
rho = 0     # Correltion parameter (NB: doesn't work for 1 or -1; degenerate hull)

# Generate Brownian motion
dW1 = np.random.normal(0, sqrtdt, N)
dW2 = rho * dW1 + np.sqrt(1 - rho * rho) * np.random.normal(0, sqrtdt, N)
W1 = dW1.cumsum()
W2 = dW2.cumsum()
W = np.array([W1, W2]).T
Wpts = W.reshape(-1, 1, 2)
segments = np.concatenate([Wpts[:-1], Wpts[1:]], axis=1)

# Animate
W1m = W1.min() - 0.1; W1M = W1.max() + 0.1; W2m = W2.min() - 0.1; W2M = W2.max() + 0.1
def animate(num):
    ax.clear()
    plt.xlim([W1m, W1M])
    plt.ylim([W2m, W2M])
    lc = LineCollection(segments[: num + 1])
    lc.set_array(np.linspace(0, 1, N))
    line = ax.add_collection(lc)
    # Generate convex hull
    hull = ConvexHull(W[: max(3, num + 1)]) # Maximum here because ConvexHull requires this size
    # Plotting convex hull
    hullCoords = list()
    for simplex in hull.simplices:
        hullCoords += list(simplex)
        plt.plot(W[simplex, 0], W[simplex, 1], "k", linewidth = 0.8)
    plt.fill(W[hull.vertices, 0], W[hull.vertices, 1], "b", alpha = 0.09)

# Plotting
plt.style.use("bmh")
fig, ax = plt.subplots(1, 1, figsize = (12, 12))#, dpi = 350)
ax.set_aspect("equal")

# Saving (requires ffmpeg unless saved as a `.gif`)
animation_1 = animation.FuncAnimation(fig, animate, interval = 3, frames = 20000)
animation_1.save("conv.mp4")
plt.show()


# Animate
W1m = W1.min() - 0.1; W1M = W1.max() + 0.1; W2m = W2.min() - 0.1; W2M = W2.max() + 0.1
def animate(num):
    ax.clear()
    plt.xlim([W1m, W1M])
    plt.ylim([W2m, W2M])
    lc = LineCollection(segments[: num + 1])
    lc.set_array(np.linspace(0, 1, N))
    line = ax.add_collection(lc)
    # Generate convex hull
    hull = ConvexHull(W[: max(3, num + 1)]) # Maximum here because ConvexHull requires this size
    # Plotting convex hull
    hullCoords = list()
    for simplex in hull.simplices:
        hullCoords += list(simplex)
        plt.plot(W[simplex, 0], W[simplex, 1], "k", linewidth = 0.8)
    plt.fill(W[hull.vertices, 0], W[hull.vertices, 1], "b", alpha = 0.09)

# Plotting
plt.style.use("bmh")
fig, ax = plt.subplots(1, 1, figsize = (12, 12))#, dpi = 350)
ax.set_aspect("equal")

# Saving (requires ffmpeg unless saved as a `.gif`)
animation_1 = animation.FuncAnimation(fig, animate, interval = 3, frames = N)
animation_1.save("conv.mp4")
plt.show()

