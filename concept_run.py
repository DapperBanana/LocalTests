
import matplotlib.pyplot as plt
import numpy as np

# Number of steps in the walk
n_steps = 1000

# Generate random steps
steps = np.random.choice([-1, 1], size=n_steps)
walk = np.cumsum(steps)

# Plot the random walk
plt.figure(figsize=(10, 5))
plt.plot(walk)
plt.title('Random Walk Plot')
plt.xlabel('Steps')
plt.ylabel('Position')
plt.grid(True)
plt.show()
