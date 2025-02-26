import numpy as np
import matplotlib.pyplot as plt

# Constants
L = 32          # Lattice size (L x L)
J = 1.0         # Interaction strength
kB = 1.0        # Boltzmann constant
n_steps = 20000 # Monte Carlo steps per temperature (for measurement)
eq_steps = 10000 # Number of equilibration steps
n_temp = 20     # Number of temperature points
T_min, T_max = 1.0, 5.0  # Temperature range

# Initialize lattice with random spins (+1 or -1)
def initialize_lattice(L):
    return np.random.choice([1, -1], size=(L, L))

# Calculate total energy of the entire lattice
def calculate_total_energy(lattice):
    L = len(lattice)
    energy = 0
    for i in range(L):
        for j in range(L):
            spin = lattice[i, j]
            neighbors = (lattice[(i + 1) % L, j] + lattice[(i - 1) % L, j] +
                         lattice[i, (j + 1) % L] + lattice[i, (j - 1) % L])
            energy -= J * spin * neighbors
    return energy / 2  # Avoid double-counting

# Compute the change in energy for flipping a single spin
def delta_energy(lattice, i, j):
    L = len(lattice)
    spin = lattice[i, j]
    neighbors = (lattice[(i + 1) % L, j] + lattice[(i - 1) % L, j] +
                 lattice[i, (j + 1) % L] + lattice[i, (j - 1) % L])
    # Flipping spin s -> -s changes energy by 2 * J * s * (sum of neighbors)
    return 2.0 * J * spin * neighbors

# Metropolis step that updates E and M locally
def metropolis_step(lattice, E, M, T):
    """
    lattice: 2D array of spins
    E: current total energy of the lattice
    M: current total spin (sum of all spins)
    T: temperature

    Returns: updated (E, M)
    """
    L = len(lattice)
    i, j = np.random.randint(0, L, 2)  # pick a random site
    dE = delta_energy(lattice, i, j)   # energy change if we flip this spin

    # Metropolis acceptance criterion
    if dE < 0 or np.random.rand() < np.exp(-dE / (kB * T)):
        # Flip the spin
        spin_before = lattice[i, j]
        lattice[i, j] = -spin_before

        # Update total energy
        E += dE

        # Update total spin: flipping +1 -> -1 => change of -2
        #                   flipping -1 -> +1 => change of +2
        M += -2 * spin_before

    return E, M

def simulate_ising(T_range):
    magnetizations = []
    energies = []
    energy_squares = []
    configs = {}

    for T in T_range:
        # Initialize lattice and calculate initial E, M
        lattice = initialize_lattice(L)
        E = calculate_total_energy(lattice)
        M = np.sum(lattice)  # total spin

        # Equilibration phase (discard these steps)
        for _ in range(eq_steps):
            E, M = metropolis_step(lattice, E, M, T)

        # Reset accumulators
        E_total = 0.0
        E2_total = 0.0
        M_total = 0.0

        # Measurement phase
        for step in range(n_steps):
            E, M = metropolis_step(lattice, E, M, T)

            # Accumulate E, E^2, and M for averaging
            E_total += E
            E2_total += E * E
            M_total += M

            # Store a configuration snapshot at midpoint
            if step == n_steps // 2:
                configs[T] = lattice.copy()

        # Compute average energy, average energy^2, and average magnetization
        avg_E = E_total / n_steps
        avg_E2 = E2_total / n_steps
        avg_M = M_total / n_steps / (L * L)  # normalize M by L^2

        magnetizations.append(avg_M)
        energies.append(avg_E)
        energy_squares.append(avg_E2)

    return np.array(magnetizations), np.array(energies), np.array(energy_squares), configs

# Main execution
temperatures = np.linspace(T_min, T_max, n_temp)
magnetizations, energies, energy_squares, configs = simulate_ising(temperatures)

# Compute specific heat, normalized by L^2
specific_heat = (energy_squares - energies**2) / (kB * temperatures**2 * (L**2))

# --- Plotting ---

# 1. Magnetization vs Temperature
plt.figure(figsize=(6, 5))
plt.plot(temperatures, magnetizations, 'b.-')
plt.xlabel('Temperature (T)')
plt.ylabel('Magnetization per spin (M)')
plt.title('Magnetization vs Temperature')
plt.grid(True)
plt.show()

# 2. Specific Heat vs Temperature
plt.figure(figsize=(6, 5))
plt.plot(temperatures, specific_heat, 'r.-')
plt.xlabel('Temperature (T)')
plt.ylabel('Specific Heat (C_v)')
plt.title('Specific Heat vs Temperature')
plt.grid(True)
plt.show()

# 3. Spin Configurations at Selected Temperatures
selected_temps = np.array([1.5, 2.3, 4.0])
selected_temps = [temperatures[np.argmin(np.abs(temperatures - T))] for T in selected_temps]

for T in selected_temps:
    plt.figure(figsize=(4, 4))
    config = configs[T]
    plt.imshow(config, cmap='gray', interpolation='none')
    plt.title(f'Spins at T = {T}')
    plt.axis('off')
    plt.show()

# --- Output Analysis ---
print("\nAnalysis:")
print("(a) Magnetization per spin vs. Temperature:")
print("   - Magnetization is high (close to ±1) at low temperatures (ordered phase).")
print("   - Near Tc (≈ 2.269), magnetization drops sharply to near zero (disordered phase).")
print("   - Indicates a phase transition from ferromagnetic to paramagnetic behavior.")

print("(b) Spin Configurations:")
print("   - At low T (e.g., 1.5), spins are mostly aligned (ferromagnetic).")
print("   - Near Tc (e.g., 2.3), domain structures form.")
print("   - At high T (e.g., 4.0), spins are randomly oriented (paramagnetic).")

print("(c) Specific Heat:")
print("   - Specific heat peaks near Tc (≈ 2.269), indicating a phase transition.")
print("   - The peak arises from large energy fluctuations near the critical point.")
