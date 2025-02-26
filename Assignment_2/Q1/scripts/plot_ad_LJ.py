import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the RDF data, skipping the header line
data1 = np.loadtxt('300k_LJ/xypr_b001_t002_u001', skiprows=1)  # 300K
data2 = np.loadtxt('500k_LJ/xypr_b001_t002_u001', skiprows=1)  # 500K
data3 = np.loadtxt('800k_LJ/xypr_b001_t002_u001', skiprows=1)  # 800K

# Extract x, y, and z columns from the data
x1, y1, z1 = data1[:, 0], data1[:, 1], data1[:, 2]
x2, y2, z2 = data2[:, 0], data2[:, 1], data2[:, 2]
x3, y3, z3 = data3[:, 0], data3[:, 1], data3[:, 2]

# Create a new figure for 3D plotting
fig = plt.figure(figsize=(18, 6))

# Subplot for 300K
temps = [(x1, y1, z1, '300K', 'viridis'), (x2, y2, z2, '500K', 'plasma'), (x3, y3, z3, '800K', 'coolwarm')]

for i, (x, y, z, title, cmap) in enumerate(temps, 1):
    ax = fig.add_subplot(1, 3, i, projection='3d')
    scatter = ax.scatter3D(x, y, z, c=z, cmap=cmap, alpha=0.8, s=20)
    cbar = fig.colorbar(scatter, ax=ax, pad=0.15)
    cbar.set_label('Z-value')
    ax.set_xlabel('X', labelpad=10)
    ax.set_ylabel('Y', labelpad=10)
    ax.set_zlabel('Z', labelpad=10)
    ax.set_title(f'Atomic Distribution at {title}', pad=15)
    ax.set_xlim(np.min(x), np.max(x))
    ax.set_ylim(np.min(y), np.max(y))
    ax.set_zlim(np.min(z), np.max(z) * 1.2)
    ax.view_init(elev=30, azim=45)

# Adjust layout
plt.subplots_adjust(left=0.05, right=0.95, wspace=0.3)

# Save the plot to a file
plt.savefig("atomic_distribution_3d.png", dpi=300)
