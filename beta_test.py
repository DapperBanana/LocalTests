
import matplotlib.pyplot as plt
import numpy as np

# Set the number of steps for the random walk
num_steps = 1000

# Generate random steps
steps = np.random.randint(-1, 2, num_steps)
walk = np.cumsum(steps)

# Plot the random walk
plt.figure(figsize=(10, 6))
plt.plot(walk, linewidth=0.5)
plt.title("Random Walk")
plt.xlabel("Steps")
plt.ylabel("Position")
plt.grid(True)
plt.show()
