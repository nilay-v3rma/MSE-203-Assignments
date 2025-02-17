import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# ----------------------- Data Loading & Preparation ---------------------------
# Load CSV file
csv_file = "deform/stress_strain.csv"
df = pd.read_csv(csv_file)

# Extract relevant columns
strain = df["v_strain"]
stress = df["von_mises_stress"]

# Apply Savitzky-Golay smoothing to reduce noise
smoothed_stress = savgol_filter(stress, window_length=101, polyorder=3)

# ----------------------- Elastic Region Analysis ------------------------------
# Define elastic region limit
elastic_end_idx = 5963
elastic_strain = strain[:elastic_end_idx + 1]
elastic_stress = stress[:elastic_end_idx + 1]

# Perform linear regression
slope, intercept = np.polyfit(elastic_strain, elastic_stress, 1)
linear_model = np.poly1d([slope, intercept])
fitted_stress = linear_model(elastic_strain)

# Elastic modulus (slope of linear fit)
elastic_modulus = slope  # GPa

# ----------------------- Yield Point Determination ---------------------------
# Define 0.2% offset line
offset = 0.002
all_strain_for_offset = np.array(strain)
offset_line = linear_model(all_strain_for_offset - offset)

# Locate yield point (intersection of stress-strain curve with offset line)
stress_after_elastic = np.array(stress[elastic_end_idx:])
offset_line_after_elastic = offset_line[elastic_end_idx:]
differences = stress_after_elastic - offset_line_after_elastic
crossings = np.where(differences > 0)[0]

if crossings.size > 0:
    crossing_idx = crossings[0] + elastic_end_idx
    yield_strain = strain[crossing_idx]
    yield_stress = stress[crossing_idx]
    print("hi")
else:
    crossing_idx, yield_strain, yield_stress = len(strain) - 1, strain.iloc[-1], stress.iloc[-1]

# Display results
print(
    f"Yield Point Index: {crossing_idx}\n"
    f"Yield Strain: {yield_strain:.4f}\n"
    f"Yield Stress: {yield_stress:.4f}\n"
    f"Elastic Modulus: {elastic_modulus:.2f} GPa"
)

# -------------------------------- Plotting ------------------------------------
plt.figure(figsize=(10, 6), dpi=120)
plt.title("Stress-Strain Curve with Yield Point Identification", fontsize=14)

# Plot raw and smoothed stress-strain data
plt.plot(strain, stress, 'o', markersize=2, color='blue', alpha=0.5, label='Raw Data')
plt.plot(strain, smoothed_stress, '-', linewidth=2, color='red', label='Smoothed Data', zorder=2)

# Highlight elastic and plastic regions
plt.axvspan(0, strain[elastic_end_idx + 1], color='lightgreen', alpha=0.3, label="Elastic Region")
plt.axvspan(strain[elastic_end_idx + 1], strain.iloc[-1], color='lightcoral', alpha=0.3, label="Plastic Region")

# Plot elastic linear fit
plt.plot(elastic_strain, fitted_stress, '--', color='green', linewidth=1.5, label=f'Linear Fit (E = {elastic_modulus:.2f})')

# Plot offset line
plt.plot(strain, offset_line, '--', color='purple', linewidth=1.5, label='0.2% Offset Line', zorder=3)

# Mark yield point with higher z-order
plt.scatter(yield_strain, yield_stress, color='black', s=80, marker='x', label=f'Yield Point\n({yield_strain:.4f}, {yield_stress:.4f})', zorder=3)

# Annotate yield point
plt.annotate(
    "Yield Point",
    xy=(yield_strain, yield_stress),
    xytext=(-40, 20),
    textcoords="offset points",
    ha='center',
    fontsize=10,
    arrowprops=dict(arrowstyle="->", color="black")
)
# Set y-axis limit based on data
plt.ylim(0, max(stress) * 1.1)
# Labels, grid, and legend
plt.xlabel("Strain", fontsize=12)
plt.ylabel("Von Mises Stress", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="upper right", fontsize=10, framealpha=0.9)

# Save and display plot
plt.tight_layout()
plt.savefig("stress_strain_plot_enhanced.png", dpi=300, bbox_inches='tight')
