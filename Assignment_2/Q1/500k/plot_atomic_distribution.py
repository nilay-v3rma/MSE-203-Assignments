import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('xypr_b001_t002_u001', skiprows=1)

# Extract x, y, and z columns from the data
x = data[:, 0]
y = data[:, 1]
z = data[:, 2]

# Create a new figure for 3D plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Create a scatter plot in 3D
#   - c=z: color points by their z-value
#   - cmap='viridis': use the 'viridis' colormap
#   - alpha=0.8: slight transparency so overlapping points are more visible
#   - s=20: point size
scatter_plot = ax.scatter3D(
    x, y, z,
    c=z,
    cmap='viridis',
    alpha=0.8,
    s=20
)

# Add a colorbar to indicate the mapping of colors to z-values
cbar = fig.colorbar(scatter_plot, ax=ax, pad=0.1)
cbar.set_label('Z-value')

# Label axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Atomic Spatial Distribution')

# Set axis limits for clarity (optional)
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(y), np.max(y))
ax.set_zlim(np.min(z), np.max(z) * 1.2)

# Adjust the viewing angle (optional)
ax.view_init(elev=30, azim=45)

# Save the plot to a file (optional)
plt.savefig("image_atomic_distribution_3d.png", dpi=300)
