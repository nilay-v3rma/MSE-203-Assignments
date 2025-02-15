import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# ----------------------- Data Loading & Preparation ---------------------------
# Load the CSV file
file_path = "msd_data_100.csv"  # Update with your CSV file path
df = pd.read_csv(file_path)

# Extract relevant columns
time = df["time"]
msd = df["msd"]

# ----------------------- Perform Linear Fit in the Middle Region ---------------------------
# Define the middle region for fitting (adjust indices as needed)
middle_start, middle_end = len(time) // 4, 3 * len(time) // 4
slope, intercept, _, _, _ = linregress(time[middle_start:middle_end], msd[middle_start:middle_end])

# Generate fitted line for visualization
fitted_msd = slope * time[middle_start:middle_end] + intercept

# ----------------------- Plotting MSD vs Time ---------------------------
plt.figure(figsize=(8, 6))
plt.plot(time, msd, linestyle='-', color='b', label=f"Polymer (N=100)")
plt.plot(time[middle_start:middle_end], fitted_msd, linestyle='--', color='r', label="Linear Fit Region")

# Add details
plt.xlabel("Time (t)", fontsize=14)
plt.ylabel("Mean Squared Displacement (MSD)", fontsize=14)
plt.title("MSD vs. Time (Chain Length N=100)", fontsize=16)
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.6)

# Display slope in the plot
slope_text = f"Slope: {slope:.5f}"
plt.text(0.1 * max(time), 0.5 * max(msd), slope_text, fontsize=12, color='red', bbox=dict(facecolor='white', alpha=0.5))

# Save the figure
plt.savefig("msd_time.png", dpi=300)
