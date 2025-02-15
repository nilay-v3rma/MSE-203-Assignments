import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
from scipy.stats import linregress

# ----------------------- Data Loading & Preparation ---------------------------
# Load the CSV file
file_path = "data.csv"  # Update with your CSV file path
df = pd.read_csv(file_path)

# Extract relevant columns
strain = df["Strain"]
stress = df["-pxx/10000"]

# Apply Savitzky-Golay smoothing to reduce noise
smoothed_stress = savgol_filter(
    stress, 
    window_length=15, 
    polyorder=3
)

# ----------------------- Elastic Region Analysis ------------------------------
# Fit linear regression to the initial elastic region (indices 0 to 140)
elastic_end_idx = 120
elastic_strain = strain[:elastic_end_idx + 1]
elastic_stress = smoothed_stress[:elastic_end_idx + 1]

slope, intercept = np.polyfit(elastic_strain, elastic_stress, 1)
linear_model = np.poly1d([slope, intercept])
fitted_stress = linear_model(elastic_strain)

# Shift x-values for visual distinction of the fitted line (offset for plotting)
elastic_strain_shifted = elastic_strain + 0.002

# ----------------------- Yield Point Determination ---------------------------
# Find yield point as the intersection beyond elastic region
post_elastic_stress = smoothed_stress[elastic_end_idx:]
post_elastic_fit = fitted_stress[elastic_end_idx:]

deviation = np.abs(post_elastic_stress - post_elastic_fit)
yield_idx = np.argmin(deviation) + elastic_end_idx  # Absolute index
yield_stress = smoothed_stress[yield_idx]
yield_strain = strain[yield_idx]

print(
    f"Yield Point Index: {yield_idx}\n"
    f"Yield Strain: {yield_strain:.4f}\n"
    f"Yield Stress: {yield_stress:.4f}"
)

# -------------------------------- Plotting ------------------------------------
plt.figure(figsize=(9, 5), dpi=120)
plt.title("Stress-Strain Curve with Yield Point Identification", fontsize=14, pad=20)

# Plot raw and smoothed data
plt.plot(
    strain, 
    stress, 
    marker='o', 
    markersize=3, 
    linestyle='-', 
    linewidth=1.2, 
    color='royalblue', 
    alpha=0.6, 
    label="Raw Data"
)
plt.plot(
    strain, 
    smoothed_stress, 
    linestyle='-', 
    linewidth=2, 
    color='red', 
    label="Smoothed Data"
)

# Highlight elastic and plastic regions
plt.axvspan(
    0, 
    strain[elastic_end_idx + 1], 
    color='lightgreen', 
    alpha=0.3, 
    label="Elastic Region"
)
plt.axvspan(
    strain[elastic_end_idx + 1], 
    strain.iloc[-1], 
    color='lightcoral', 
    alpha=0.3, 
    label="Plastic Region"
)

# Plot linear fit and yield point
plt.plot(
    elastic_strain_shifted, 
    fitted_stress, 
    linestyle='--', 
    color='green', 
    label=f'Linear Fit (E = {slope:.2f})'
)
plt.scatter(
    yield_strain, 
    yield_stress, 
    color='black',
    s=80,
    marker='x',
    linewidths=1,
    zorder=5,
    # Modified label to include values
    label=f'Yield Point\n({yield_strain:.4f}, {yield_stress:.4f})'  # <-- THIS LINE CHANGED
)

# Annotate yield point
plt.annotate(
    "Yield Point", 
    xy=(yield_strain, yield_stress),
    xytext=(-30, 20),
    textcoords="offset points",
    ha='center',
    fontsize=10,
    arrowprops=dict(arrowstyle="->", color="black")
)

# Axis labels and grid
plt.xlabel("Strain", fontsize=12, labelpad=10)
plt.ylabel("-pxx / 10000 (Stress)", fontsize=12, labelpad=10)
plt.grid(True, linestyle="--", alpha=0.6)

# Legend and layout
plt.legend(
    loc="upper right", 
    fontsize=10, 
    framealpha=0.9, 
    edgecolor="black",
    # Added to handle multi-line legend entries
    title="Legend",                     
    title_fontsize=11,                  
    handletextpad=0.5,                  
    columnspacing=1                     
)
plt.tight_layout()

# Save and show
plt.savefig("strain_stress_plot_annotated_neat.png", bbox_inches="tight")
