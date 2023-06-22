import numpy as np
import matplotlib.pyplot as plt

# Set lattice dimensions
N = 6  # Number of lattice points along each dimension

# Initialize lattice
lattice = np.ones((N, N))

# Define temperature range
T_range = np.linspace(0, 5, 100)  # Temperature values from 0 to 5 K

# Define number of Monte Carlo steps
num_steps = 10000

# Define magnetization list
magnetization = []

# Perform Monte Carlo simulation for each temperature
for T in T_range:
    # Perform Monte Carlo simulation
    for step in range(num_steps):
        # Randomly choose a lattice site
        i = np.random.randint(0, N)
        j = np.random.randint(0, N)

        # Calculate the change in energy if the spin is flipped
        delta_E = 2 * lattice[i, j] * (
            lattice[(i + 1) % N, j]
            + lattice[(i - 1) % N, j]
            + lattice[i, (j + 1) % N]
            + lattice[i, (j - 1) % N]
        )

        # Flip the spin with a probability according to the Metropolis-Hastings acceptance criterion
        if delta_E < 0 or np.random.rand() < np.exp(-delta_E / T):
            lattice[i, j] *= -1

    # Calculate magnetization after 10,000 iterations
    m = np.sum(lattice)
    magnetization.append(m)

# Plot and save magnetization vs temperature
plt.plot(T_range, magnetization, marker='o', linestyle='-', color='blue')
plt.xlabel('Temperature (K)')
plt.ylabel('Magnetization')
plt.title('Magnetization vs Temperature')
plt.savefig('magnetization_vs_temperature_plot.png')
plt.show()
