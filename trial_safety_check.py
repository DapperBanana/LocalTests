
import matplotlib.pyplot as plt
import numpy as np

# Number of steps in the random walk
n_steps = 100

# Generate random step sizes
step_size = np.random.randint(-1, 2, size=n_steps)

# Calculate the random walk
walk = np.cumsum(step_size)

# Plot the random walk
plt.plot(walk)
plt.title('Random Walk Plot')
plt.xlabel('Step')
plt.ylabel('Position')
plt.show()
