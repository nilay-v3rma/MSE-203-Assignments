import numpy as np
import matplotlib.pyplot as plt

# Load the RDF data, skipping the header line
data = np.loadtxt('rdf_b001_m002_u001_m002_u001', skiprows=1)  # Skip the first line

# Extract distance (r) and g(r) columns
r = data[:, 0]  # Distance in Å (first column)
g_r = data[:, 1]  # g(r) values (second column)

# Plot the RDF
plt.figure(figsize=(10, 6))  # Set figure size for clarity
plt.plot(r, g_r, 'b-', label='g(r) 500K Hard Sphere')
plt.xlabel('Distance (Å)')
plt.ylabel('Radial Distribution Function, g(r)')
plt.title('RDF for Binary Hard Sphere System at 500K')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(y=1.0, color='r', linestyle='--', alpha=0.5, label='Bulk Density')
plt.axvline(x=1.0, color='g', linestyle='--', alpha=0.5, label='Hard Sphere Diameter')

# Add some formatting for readability
plt.ylim(0, max(g_r) * 1.2)  # Set y-limit slightly above max g(r)
plt.xlim(0, max(r))  # Set x-limit to full range

# Add text annotations for key features
plt.text(1.1, max(g_r) * 0.9, f'First Peak: {g_r[np.argmax(g_r)]:.2f} at {r[np.argmax(g_r)]:.2f} Å',
         fontsize=10, verticalalignment='top')

plt.savefig("image.png")
