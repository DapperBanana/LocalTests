
import matplotlib.pyplot as plt
import numpy as np

# Set the number of steps in the random walk
num_steps = 1000

# Generate random walk data
x = np.cumsum(np.random.randn(num_steps))
y = np.cumsum(np.random.randn(num_steps))

# Plot the random walk
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Random Walk Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
