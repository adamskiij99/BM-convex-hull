# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 21:54:26 2022

@author: Administrator
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.spatial import ConvexHull

# Params
T = 1
N = 2000
dt = T / N
sqrtdt = np.sqrt(dt)

# Generate Brownian motion
dW1 = np.random.normal(0, sqrtdt, N)
dW2 = np.random.normal(0, sqrtdt, N)
dW3 = np.random.normal(0, sqrtdt, N)
W1 = dW1.cumsum()
W2 = dW2.cumsum()
W3 = dW3.cumsum()
W = np.array([W1, W2, W3]).T

# Generate convex hull and reformat W points for ease later
hull = ConvexHull(W)
Wpts = W.reshape(-1, 1, 3)
segments = np.concatenate([Wpts[:-1], Wpts[1:]], axis = 1)

# Formatting
plt.style.use("bmh")
fig = plt.figure(figsize = (12, 12), dpi = 85)
ax = fig.add_subplot(111, projection = "3d")

# Colouring/formatting line plot
lc = Line3DCollection(segments)
lc.set_array(np.linspace(0, 1, N))
lc.set_linewidth(0.5)
line = ax.add_collection(lc)

# Animate
W1m = W1.min() - 0.1; W1M = W1.max() + 0.1
W2m = W2.min() - 0.1; W2M = W2.max() + 0.1
W3m = W3.min() - 0.1; W3M = W3.max() + 0.1
def animate(num):
    ax.clear()
    ax.set_xlim3d([W1m, W1M])
    ax.set_ylim3d([W2m, W2M])
    ax.set_zlim3d([W3m, W3M])
    lc = Line3DCollection(segments[: num + 1])
    lc.set_array(np.linspace(0, 1, N))
    line = ax.add_collection(lc)
    # Generate convex hull
    hull = ConvexHull(W[: max(4, num + 1)]) # Maximum here because ConvexHull requires this size
    # Plotting convex hull
    for simplex in hull.simplices:
       plt.plot(W[simplex, 0], W[simplex, 1], W[simplex, 2], "k", linewidth = 0.3, alpha = 0.8)
       # After quite a while of tweaking data format, this is the only format for
       # verts which allows shading of the hull with Poly3DCollection. Give alpha=0
       # to the above line if you don't want the black edges, rather than comment out.
       verts = [list(zip(W[simplex, 0], W[simplex, 1], W[simplex, 2]))]
       ax.add_collection3d(Poly3DCollection(verts, alpha = 0.1))

plt.title("Convex hull of Brownian motion up to time T = 5")
ax.set_box_aspect((np.ptp(W1), np.ptp(W2), np.ptp(W3))) # For correct axis proportions
animation_1 = animation.FuncAnimation(fig, animate, interval = 10, frames = N)
animation_1.save("conv3.mp4")
plt.show()
