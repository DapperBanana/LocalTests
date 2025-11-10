
import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Number of steps in the random walk
n_steps = 100

# Generate random steps
steps = np.random.choice([-1, 1], size=n_steps)

# Calculate positions
positions = np.cumsum(steps)

# Plot the random walk
plt.figure(figsize=(10, 6))
plt.plot(positions)
plt.title('Random Walk Plot')
plt.xlabel('Step')
plt.ylabel('Position')
plt.grid(True)
plt.show()
