import numpy as np
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.collections import PolyCollection
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from stl import Mesh

# Create a new plot
figure = plt.figure()
axes = Axes3D(figure)

# Load the STL files and add the vectors to the plot
your_mesh = Mesh.from_file('Body Cap.stl')

poly = Poly3DCollection(your_mesh.vectors)
poly.set_edgecolor('black')
axes.add_collection3d(poly)

min_x = np.hstack((your_mesh.v0[:, 0].min(), your_mesh.v1[:, 0].min(), your_mesh.v2[:, 0].min())).min()
max_x = np.hstack((your_mesh.v0[:, 0].max(), your_mesh.v1[:, 0].max(), your_mesh.v2[:, 0].max())).max()

proportion = .1

percent = (max_x - min_x) * proportion
min_x -= percent
max_x += percent

min_y = np.hstack((your_mesh.v0[:, 1].min(), your_mesh.v1[:, 1].min(), your_mesh.v2[:, 1].min())).min()
max_y = np.hstack((your_mesh.v0[:, 1].max(), your_mesh.v1[:, 1].max(), your_mesh.v2[:, 1].max())).max()

percent = (max_y - min_y) * proportion
min_y -= percent
max_y += percent

min_z = np.hstack((your_mesh.v0[:, 2].min(), your_mesh.v1[:, 2].min(), your_mesh.v2[:, 2].min())).min()
max_z = np.hstack((your_mesh.v0[:, 2].max(), your_mesh.v1[:, 2].max(), your_mesh.v2[:, 2].max())).max()

percent = (max_y - min_y) * proportion
min_z -= percent
max_z += percent

# Auto scale to the mesh size
axes.set_xlim(min_x, max_x)
axes.set_ylim(min_y, max_y)
axes.set_zlim(min_z, max_z)


out = np.array(list(zip(your_mesh.v0[:, :2], your_mesh.v1[:, :2], your_mesh.v2[:, :2])))

a = out.min()

fig: Figure = plt.figure()
axes: Axes = fig.gca()
poly = PolyCollection(out)
poly.set_edgecolor('black')

axes.add_collection(poly)
axes.set_xlim(min_x, max_x)
axes.set_ylim(min_y, max_y)

# Show the plot to the screen
plt.show()
