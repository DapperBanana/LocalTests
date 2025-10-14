
import matplotlib.pyplot as plt
import numpy as np

# Set the number of steps in the random walk
num_steps = 1000

# Generate random steps
steps = np.random.choice([-1, 1], size=num_steps)
walk = np.cumsum(steps)

# Plot the random walk
plt.figure()
plt.plot(walk)
plt.title("Random Walk Plot")
plt.xlabel("Steps")
plt.ylabel("Position")
plt.show()
