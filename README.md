# Convex hull of planar and spacial Brownian motion
Generates the convex hull of 2-dimensional Brownian motion with independent coordinates. Running `convex_hull_2d_bm.py` will generate a plot like the one below.

![2dbm](https://user-images.githubusercontent.com/62266775/194130927-c427067e-c265-461d-952d-2e0f1feeee0b.png)

Fun fact: the boundary of the convex hull of a Brownian motion in the plane after any finite amount of time is almost surely $C^1$ (a continuously differentiable curve). See: Smoothness of the Convex Hull of Planar Brownian Motion (1989) by Cranston et al.

Running `ch2dbm_anim.py` will generate a similar plot to above but will also save the animation `conv.mp4` to the same folder as the file is run; this video will show the running process and convex hull, similar to below. It will take longer to run, due to each frame needing to be plotted and saved, so reserve around 10 minutes for the video to be produced. A prerequisite for this is FFmpeg, which is a video saving/conversion tool, and can be found [here](https://ffmpeg.org/download.html).

https://user-images.githubusercontent.com/62266775/194716130-8c249ba0-9d30-4aff-84c9-8ca356073cae.mp4

Running `convex_hull_3d_bm.py` will generate a plot like the one below.

![3dbm](https://user-images.githubusercontent.com/62266775/194771283-642db751-cf89-427a-a6b3-568891614528.png)
