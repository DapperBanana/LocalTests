
import matplotlib.pyplot as plt
import numpy as np

# Number of steps in the random walk
num_steps = 1000

# Generate random steps (1 or -1) for each step
steps = np.random.choice([-1, 1], size=num_steps)

# Calculate the random walk
walk = np.cumsum(steps)

# Plot the random walk
plt.plot(walk)
plt.title('Random Walk Plot')
plt.xlabel('Steps')
plt.ylabel('Value')
plt.show()
