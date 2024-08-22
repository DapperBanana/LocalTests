
import matplotlib.pyplot as plt
import numpy as np

# Set seed for reproducibility
np.random.seed(0)

# Number of steps in the random walk
n_steps = 1000

# Generate random steps (either -1 or 1)
steps = np.random.choice([-1, 1], size=n_steps)

# Calculate the random walk
walk = np.cumsum(steps)

# Plot the random walk
plt.plot(np.arange(n_steps), walk)
plt.title('Random Walk Plot')
plt.xlabel('Steps')
plt.ylabel('Position')
plt.show()
