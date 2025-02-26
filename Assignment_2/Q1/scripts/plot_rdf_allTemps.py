import numpy as np
import matplotlib.pyplot as plt

# Load the RDF data, skipping the header line
data1 = np.loadtxt('300k/rdf_b001_m002_u001_m002_u001', skiprows=1)  # 300K
data2 = np.loadtxt('500k/rdf_b001_m002_u001_m002_u001', skiprows=1)  # 500K
data3 = np.loadtxt('800k/rdf_b001_m002_u001_m002_u001', skiprows=1)  # 800K

# Extract distance (r) and g(r) columns
r1, g_r1 = data1[:, 0], data1[:, 1]  # 300K
r2, g_r2 = data2[:, 0], data2[:, 1]  # 500K
r3, g_r3 = data3[:, 0], data3[:, 1]  # 800K

# Ensure all r arrays are the same length for plotting (trim if necessary)
min_length = min(len(r1), len(r2), len(r3))
r1, g_r1 = r1[:min_length], g_r1[:min_length]
r2, g_r2 = r2[:min_length], g_r2[:min_length]
r3, g_r3 = r3[:min_length], g_r3[:min_length]

# Plot the RDF for all temperatures with transparency to emphasize overlap
plt.figure(figsize=(10, 6))
plt.plot(r1, g_r1, 'b-', label='g(r) 300K', alpha=0.5, linewidth=2)
plt.plot(r2, g_r2, 'r-', label='g(r) 500K', alpha=0.5, linewidth=2)
plt.plot(r3, g_r3, 'g-', label='g(r) 800K', alpha=0.5, linewidth=2)

# Add labels, title, and grid
plt.xlabel('Distance (Å)')
plt.ylabel('Radial Distribution Function, g(r)')
plt.title('RDF for Binary Hard Sphere System at Different Temperatures')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(y=1.0, color='k', linestyle='--', alpha=0.5, label='Bulk Density')
plt.axvline(x=1.0, color='k', linestyle='--', alpha=0.5, label='Hard Sphere Diameter')

# Add formatting for readability
plt.ylim(0, max(max(g_r1), max(g_r2), max(g_r3)) * 1.2)
plt.xlim(0, max(max(r1), max(r2), max(r3)))

# Annotate the first peak (using 300K as reference, since they overlap)
peak_idx = np.argmax(g_r1)
peak_r = r1[peak_idx]
peak_g = g_r1[peak_idx]
plt.text(peak_r + 0.1, peak_g * 0.9,
         f'First Peak: {peak_g:.2f} at {peak_r:.2f} Å',
         fontsize=10, verticalalignment='top')

# Emphasize overlap with annotation
plt.text(3.0, 1.5, 'Curves overlap due to temperature\nindependence of Hard Spheres',
         fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

# Add a vertical line at the overlap region (e.g., around the first peak)
plt.axvline(x=peak_r, color='gray', linestyle='--', alpha=0.3)

plt.savefig("rdf_all_temperatures_overlapping.png")
