
import matplotlib.pyplot as plt
import random

# Number of steps in the random walk
num_steps = 1000

# Generate random walk data
x = [0]
y = [0]
for i in range(1, num_steps):
    step = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
    x.append(x[i-1] + step[0])
    y.append(y[i-1] + step[1])

# Plot the random walk
plt.figure(figsize=(8, 6))
plt.plot(x, y, linewidth=2, color='blue')
plt.scatter(x[0], y[0], color='green', marker='o', label='Start')
plt.scatter(x[-1], y[-1], color='red', marker='o', label='End')
plt.title('Random Walk Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
