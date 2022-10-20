# Convex hull of planar and spacial Brownian motion
Generates the convex hull of 2-dimensional Brownian motion. Running `convex_hull_2d_bm.py` will generate a plot like the one below.

![2dbm](https://user-images.githubusercontent.com/62266775/194130927-c427067e-c265-461d-952d-2e0f1feeee0b.png)

Fun fact: the boundary of the convex hull of a Brownian motion in the plane after any finite amount of time is almost surely $C^1$ (a continuously differentiable curve). See: Smoothness of the Convex Hull of Planar Brownian Motion (1989) by Cranston et al.

Running `ch2dbm_anim.py` will generate a similar plot to above but will also save the animation `conv.mp4` to the same folder as the file is run; this video will show the running process and convex hull, similar to below. It will take longer to run, due to each frame needing to be plotted and saved, so reserve around 10 minutes for the video to be produced. A prerequisite for this is FFmpeg, which is a video saving/conversion tool, and can be found [here](https://ffmpeg.org/download.html).

https://user-images.githubusercontent.com/62266775/194716130-8c249ba0-9d30-4aff-84c9-8ca356073cae.mp4

Running `2d_perim_distn.py` will generate a plot of the perimeter distribution (in blue) and area distribution (in red) of the convex hull. By default, the plots will show Monte Carlo'd distributions over 50 000 samples.

![perims areas](https://user-images.githubusercontent.com/62266775/196992170-f7e9596b-0276-4735-8454-e61de0f4b289.png)

The distribution of this over time is not included, as due to scaling properties of Brownian motion, the distributions of perimeter and area over time are just rescaled versions of each other.

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

The distributions of perimeter and area of the convex hull of planar Brownian motion is an open problem. One observation is that log(perim) and log(area) appear symmetric and look bell shaped, but are not Gaussian. The means and variances are however known, even with drift. Namely, if $P(t)$ and $A(t)$ respectively denote the perimeter and area of the convex hull of planar BM run to time $t$, then $\mathbb{E}(P(t)) = \sqrt{8\pi t}$ (Takacs, 1980) and $\mathbb{E}(A(t)) = \pi t/2$ (El Bachir, 1983).

Stepping up to higher dimensions, running `convex_hull_3d_bm.py` will generate a plot like the one below.

![3dbm](https://user-images.githubusercontent.com/62266775/194771283-642db751-cf89-427a-a6b3-568891614528.png)

And running `ch3dbm_anim.py` will generate something like the animation below, saving `conv3.mp4`, also requiring FFmpeg. This, the way I've implemented it, seems to take much longer to produce.

https://user-images.githubusercontent.com/62266775/195433863-64f32ed5-c25e-47a4-83f2-165e42a81429.mp4


