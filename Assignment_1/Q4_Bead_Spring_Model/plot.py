import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ----------------------- Data Loading & Preparation ---------------------------
# Load the CSV file
def load_data(n):
    file_path = f"{n}Mers/msd_data_{n}.csv"  # Update with your CSV file path
    df = pd.read_csv(file_path)

    # Extract relevant columns
    time = df["time"]
    msd = df["msd"]

    return time,msd

time10,msd10 = load_data(10)
time100,msd100 = load_data(100)

# ----------------------- Plotting MSD vs Time ---------------------------
plt.figure(figsize=(8, 6))
plt.plot(time10, msd10, linestyle='-', color='r', label=f"Polymer (N=10)")
plt.plot(time100, msd100, linestyle='-', color='b', label=f"Polymer (N=100)")

# Add details
plt.xlabel("Time (t)", fontsize=14)
plt.ylabel("Mean Squared Displacement (MSD)", fontsize=14)
plt.title("MSD vs. Time", fontsize=16)
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.6)

# Save the figure
plt.savefig("msd_time.png", dpi=300)
