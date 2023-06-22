import numpy as np
import random

# Define the Ising model parameters
L = 10  # Length of the lattice
J = 1   # Coupling constant
beta = 1  # Inverse temperature

# Initialize the lattice randomly with spin up (+1) or spin down (-1)
lattice = np.random.choice([-1, 1], size=(L, L), replace=True)
# Define a function to calculate the energy of the system
def calculate_energy(lattice):
    energy = 0
    for i in range(L):
        for j in range(L):
            energy += -J * lattice[i, j] * (lattice[(i+1)%L, j] + lattice[(i-1)%L, j] + lattice[i, (j+1)%L] + lattice[i, (j-1)%L])
    return energy
# Define a function to perform a Markov chain step using the Metropolis-Hastings algorithm
def markov_chain_step(lattice, beta):
    i = random.randint(0, L-1)
    j = random.randint(0, L-1)
    
    # Calculate the energy difference if we flip the spin at position (i, j)
    delta_energy = 2 * J * lattice[i, j] * (lattice[(i+1)%L, j] + lattice[i, (j+1)%L] + lattice[(i-1)%L, j] + lattice[i, (j-1)%L])
    
    # Accept or reject the flip based on the Metropolis-Hastings acceptance criterion
    if delta_energy <= 0 or random.random() < np.exp(-beta * delta_energy):
        lattice[i, j] *= -1

# Run the Markov chain to simulate the dynamics of the Ising model
num_steps = 1

for step in range(num_steps):
    markov_chain_step(lattice, beta)

# Print the final state of the lattice
print("Final state of the lattice:")
print(lattice)
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def visualize_lattice(lattice, save_path=None):
    # Define the two colors for +1 and -1 spins
    colors = ["crimson", "rosybrown"]
    
    # Create a custom colormap with the specified colors
    cmap = ListedColormap(colors)
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the lattice using colors
    im = ax.imshow(lattice, cmap=cmap)
    
    # Add colorbar
    
    # Set axis labels
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    if save_path is not None:
        plt.savefig(save_path)
    # Set plot title
    
    # Display the plot
    plt.show()
    
# Assuming you have an Ising model lattice stored in the 'lattice' variable
visualize_lattice(lattice, save_path="MCMC1.png")
