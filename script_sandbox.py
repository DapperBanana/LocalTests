
import matplotlib.pyplot as plt
import numpy as np

# Number of steps in the random walk
num_steps = 1000

# Generate random walk data
x = np.cumsum(np.random.randn(num_steps))
y = np.cumsum(np.random.randn(num_steps))

# Plot the random walk
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title("Random Walk")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
