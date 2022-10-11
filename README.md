# Convex hull of planar and spacial Brownian motion
Generates the convex hull of 2-dimensional Brownian motion with independent coordinates. Running `convex_hull_2d_bm.py` will generate a plot like the one below.

![2dbm](https://user-images.githubusercontent.com/62266775/194130927-c427067e-c265-461d-952d-2e0f1feeee0b.png)

Fun fact: the boundary of the convex hull of a Brownian motion in the plane after any finite amount of time is almost surely $C^1$ (a continuously differentiable curve). See: Smoothness of the Convex Hull of Planar Brownian Motion (1989) by Cranston et al.

Running `ch2dbm_anim.py` will generate a similar plot to above but will also save the animation `conv.mp4` to the same folder as the file is run; this video will show the running process and convex hull, similar to below. It will take longer to run, due to each frame needing to be plotted and saved, so reserve around 10 minutes for the video to be produced. A prerequisite for this is FFmpeg, which is a video saving/conversion tool, and can be found [here](https://ffmpeg.org/download.html).

https://user-images.githubusercontent.com/62266775/194716130-8c249ba0-9d30-4aff-84c9-8ca356073cae.mp4

Running `2d_perim_distn.py` will generate some plots of the perimeter distribution (in blue) and area distribution (in red) of the convex hull. By default, the plots will show Monte Carlo'd distributions of the perimeter and area over ten time steps: 0.1, 0.2, ..., 1.

![areaperim](https://user-images.githubusercontent.com/62266775/195159967-c552eb78-3f3b-452b-9c74-d3127cf773f5.png)

Other properties can be explored in the console after running this. For example:
```python
x0 = T / tSteps
x = np.linspace(x0, T, tSteps)
y = np.zeros(tSteps)
for i in range(tSteps):
    y[i] = np.var(A[i])
plt.plot(x, y)
```
will plot the variance of the area over time.

I'm keen to know what the distribution of these are. It has been suggested that this is a Tracy-Widom distribution by friends I have shared this with, however I am yet to explore the mathematics. It would also be interesting to find a PDE for which this family of probability distributions is the solution. Please get in touch if you have any ideas on how to approach either of these!

Stepping up to higher dimensions, running `convex_hull_3d_bm.py` will generate a plot like the one below.

![3dbm](https://user-images.githubusercontent.com/62266775/194771283-642db751-cf89-427a-a6b3-568891614528.png)
