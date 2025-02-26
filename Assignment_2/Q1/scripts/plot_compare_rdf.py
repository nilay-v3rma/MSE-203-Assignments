import numpy as np
import matplotlib.pyplot as plt

# Load the RDF data, skipping the header line
data_lj = np.loadtxt('rdf_LJ', skiprows=1)  # Skip the first line
data_hs = np.loadtxt('rdf_HS', skiprows=1)

# Extract distance (r) and g(r) columns for both datasets
r_lj = data_lj[:, 0]  # Distance in Å (first column of LJ)
g_r_lj = data_lj[:, 1]  # g(r) values for LJ

r_hs = data_hs[:, 0]  # Distance in Å (first column of HS)
g_r_hs = data_hs[:, 1]  # g(r) values for HS

# Plot the RDF for both systems
plt.figure(figsize=(10, 6))  # Set figure size for clarity
plt.plot(r_lj, g_r_lj, 'b-', label='Lennard-Jones (LJ) 300K')
plt.plot(r_hs, g_r_hs, 'r--', label='Hard Sphere (HS) 300K')

plt.xlabel('Distance (Å)')
plt.ylabel('Radial Distribution Function, g(r)')
plt.title('Comparison of RDF for Lennard-Jones and Hard Sphere Systems at 300K')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(y=1.0, color='gray', linestyle='--', alpha=0.5, label='Bulk Density')
plt.axvline(x=1.0, color='g', linestyle='--', alpha=0.5, label='Hard Sphere Diameter')

# Set limits for clarity
plt.ylim(0, max(max(g_r_lj), max(g_r_hs)) * 1.2)  # Adjust y-limit based on highest peak
plt.xlim(0, max(max(r_lj), max(r_hs)))  # Adjust x-limit based on data range

# Add annotations for key features
plt.text(r_lj[np.argmax(g_r_lj)], max(g_r_lj) * 0.9, f'First Peak (LJ): {g_r_lj[np.argmax(g_r_lj)]:.2f}',
         fontsize=10, verticalalignment='top', color='blue')
plt.text(r_hs[np.argmax(g_r_hs)], max(g_r_hs) * 0.9, f'First Peak (HS): {g_r_hs[np.argmax(g_r_hs)]:.2f}',
         fontsize=10, verticalalignment='top', color='red')

plt.savefig("rdf_comparison.png")
