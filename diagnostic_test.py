
import matplotlib.pyplot as plt
import numpy as np

# Number of steps in the random walk
num_steps = 1000

# Generate random steps
steps = np.random.choice([-1, 1], size=num_steps)
walk = np.cumsum(steps)

# Plot random walk
plt.figure(figsize=(10, 6))
plt.plot(walk)
plt.title('Random Walk Plot')
plt.xlabel('Step')
plt.ylabel('Position')
plt.grid(True)
plt.show()
