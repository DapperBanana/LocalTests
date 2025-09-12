
import matplotlib.pyplot as plt
import numpy as np

# Number of steps in the random walk
n_steps = 100

# Generate random steps for x and y coordinates
x_steps = np.random.choice([-1, 1], size=n_steps)
y_steps = np.random.choice([-1, 1], size=n_steps)

# Calculate cumulative sum to get the random walk path
x_path = np.cumsum(x_steps)
y_path = np.cumsum(y_steps)

# Plot the random walk path
plt.figure()
plt.plot(x_path, y_path)
plt.title("Random Walk Plot")
plt.xlabel("X-coordinate")
plt.ylabel("Y-coordinate")
plt.show()
