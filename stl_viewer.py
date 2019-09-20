import numpy as np
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.collections import PolyCollection
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from stl import Mesh


def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5 * max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


def get_limit(mesh, column, scale=.1):
    min_val = np.hstack((mesh.v0[:, column].min(), mesh.v1[:, column].min(), mesh.v2[:, column].min())).min()
    max_val = np.hstack((mesh.v0[:, column].max(), mesh.v1[:, column].max(), mesh.v2[:, column].max())).max()

    percent = (max_val - min_val) * scale
    min_val -= percent
    max_val += percent

    return max_val, min_val


def get_2d_bounding_box(mesh):
    x, y, z = get_limit(mesh, 0, 0), get_limit(mesh, 1, 0), get_limit(mesh, 2, 0)

    x_min = x[1]
    y_min = y[1]

    x_width = x[0] - x[1]
    y_width = y[0] - y[1]

    return x_min, x_width, y_min, y_width


def get_2d_box(mesh):
    x, width, y, height = get_2d_bounding_box(mesh)

    rect = Rectangle((x, y), width, height)
    rect.set_edgecolor('red')
    rect.set_facecolor('none')

    return rect


# Load the STL files and add the vectors to the plot
your_mesh = Mesh.from_file('Body Cap.stl')

# Create a new plot
figure = plt.figure()
axes: Axes3D = Axes3D(figure)

poly = Poly3DCollection(your_mesh.vectors)
poly.set_edgecolor('black')
axes.add_collection3d(poly)

x_lim, y_lim, z_lim = get_limit(your_mesh, 0), get_limit(your_mesh, 1), get_limit(your_mesh, 2)

# Auto scale to the mesh size
axes.set_xlim(*x_lim)
axes.set_ylim(*y_lim)
axes.set_zlim(*z_lim)
set_axes_equal(axes)

out = np.array(list(zip(your_mesh.v0[:, :2], your_mesh.v1[:, :2], your_mesh.v2[:, :2])))

fig: Figure = plt.figure()
axes: Axes = fig.gca()
poly = PolyCollection(out)
poly.set_edgecolor('black')

axes.add_collection(poly)
axes.add_patch(get_2d_box(your_mesh))

axes.set_xlim(*x_lim[::-1])
axes.set_ylim(*y_lim[::-1])
axes.set_aspect('equal')

# Show the plot to the screen
plt.show()
