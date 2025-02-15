import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter

# ----------------------- Data Loading & Preparation ---------------------------
# Function to load and process data

def load_and_process(file_path):
    df = pd.read_csv(file_path)
    strain = df["Strain"]
    stress = df["-pxx/10000"]
    smoothed_stress = savgol_filter(stress, window_length=15, polyorder=3)
    return strain, smoothed_stress

# Load data for different temperatures
file_paths = {
    "300K": "data_300.csv",
    "600K": "data_600.csv",
    "900K": "data_900.csv"
}

# Store data
data = {label: load_and_process(path) for label, path in file_paths.items()}

# ----------------------- Plotting ---------------------------
plt.figure(figsize=(9, 5), dpi=120)
plt.title("Stress-Strain Curves for Different Temperatures", fontsize=14, pad=20)

# Define colors
colors = {"300K": "blue", "600K": "red", "900K": "green"}

# Plot data for each temperature
for label, (strain, smoothed_stress) in data.items():
    plt.plot(
        strain,
        smoothed_stress,
        linestyle='-',
        linewidth=2,
        color=colors[label],
        label=f"{label}"
    )

# Axis labels and grid
plt.xlabel("Strain", fontsize=12, labelpad=10)
plt.ylabel("-pxx / 10000 (Stress)", fontsize=12, labelpad=10)
plt.grid(True, linestyle="--", alpha=0.6)

# Legend and layout
plt.legend(fontsize=10, framealpha=0.9, edgecolor="black")
plt.tight_layout()

# Save and show
plt.savefig("stress_strain_comparison.png", bbox_inches="tight")
