
import matplotlib.pyplot as plt
import numpy as np

# Number of steps in the random walk
num_steps = 1000

# Generate random steps
rand_steps = np.random.choice([-1, 1], num_steps)

# Calculate random walk
random_walk = np.cumsum(rand_steps)

# Plot the random walk
plt.figure(figsize=(10, 6))
plt.plot(random_walk)
plt.title('Random Walk Plot')
plt.xlabel('Step')
plt.ylabel('Position')
plt.grid(True)
plt.show()
