import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the atomic distribution data, skipping the header line
data_lj = np.loadtxt('ad_LJ', skiprows=1)
data_hs = np.loadtxt('ad_HS', skiprows=1)

# Extract x, y, and z columns from the data
x_lj, y_lj, z_lj = data_lj[:, 0], data_lj[:, 1], data_lj[:, 2]
x_hs, y_hs, z_hs = data_hs[:, 0], data_hs[:, 1], data_hs[:, 2]

# Create a new figure for 3D plotting
fig = plt.figure(figsize=(14, 6))

# Subplot for Lennard-Jones (LJ) system
ax1 = fig.add_subplot(121, projection='3d')
scatter_lj = ax1.scatter3D(
    x_lj, y_lj, z_lj,
    c=z_lj,
    cmap='viridis',
    alpha=0.8,
    s=20
)
cbar1 = fig.colorbar(scatter_lj, ax=ax1, pad=0.15)
cbar1.set_label('Z-value')
ax1.set_xlabel('X', labelpad=10)
ax1.set_ylabel('Y', labelpad=10)
ax1.set_zlabel('Z', labelpad=10)
ax1.set_title('Lennard-Jones Atomic Distribution', pad=15)
ax1.set_xlim(np.min(x_lj), np.max(x_lj))
ax1.set_ylim(np.min(y_lj), np.max(y_lj))
ax1.set_zlim(np.min(z_lj), np.max(z_lj) * 1.2)
ax1.view_init(elev=30, azim=45)

# Subplot for Hard Sphere (HS) system
ax2 = fig.add_subplot(122, projection='3d')
scatter_hs = ax2.scatter3D(
    x_hs, y_hs, z_hs,
    c=z_hs,
    cmap='plasma',
    alpha=0.8,
    s=20
)
cbar2 = fig.colorbar(scatter_hs, ax=ax2, pad=0.15)
cbar2.set_label('Z-value')
ax2.set_xlabel('X', labelpad=10)
ax2.set_ylabel('Y', labelpad=10)
ax2.set_zlabel('Z', labelpad=10)
ax2.set_title('Hard Sphere Atomic Distribution', pad=15)
ax2.set_xlim(np.min(x_hs), np.max(x_hs))
ax2.set_ylim(np.min(y_hs), np.max(y_hs))
ax2.set_zlim(np.min(z_hs), np.max(z_hs) * 1.2)
ax2.view_init(elev=30, azim=45)

# Adjust layout
plt.subplots_adjust(left=0.05, right=0.95, wspace=0.3)

# Save the plot to a file
plt.savefig("atomic_distribution_comparison_3d.png", dpi=300)
