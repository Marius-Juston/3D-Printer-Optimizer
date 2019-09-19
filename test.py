import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
from mpl_toolkits.mplot3d import axes3d
import numpy as np

# These will be (200, 4), (200, 4), and (4)
freq_data = np.linspace(0,300,200)[:,None] * np.ones(4)[None,:]
amp_data = np.random.rand(200*4).reshape((200,4))
rad_data = np.linspace(0,2,4)

verts = []
for irad in range(len(rad_data)):
    # I'm adding a zero amplitude at the beginning and the end to get a nice
    # flat bottom on the polygons
    xs = np.concatenate([[freq_data[0,irad]], freq_data[:,irad], [freq_data[-1,irad]]])
    ys = np.concatenate([[0],amp_data[:,irad],[0]])
    verts.append(list(zip(xs, ys)))

print(verts)
poly = PolyCollection(verts, facecolors = ['r', 'g', 'c', 'y'])


poly.set_alpha(0.7)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# The zdir keyword makes it plot the "z" vertex dimension (radius)
# along the y axis. The zs keyword sets each polygon at the
# correct radius value.
ax.add_collection3d(poly, zs=rad_data, zdir='y')

ax.set_xlim3d(freq_data.min(), freq_data.max())
ax.set_xlabel('Frequency')
ax.set_ylim3d(rad_data.min(), rad_data.max())
ax.set_ylabel('Radius')
ax.set_zlim3d(amp_data.min(), amp_data.max())
ax.set_zlabel('Amplitude')

plt.show()