
import matplotlib.pyplot as plt
import random

# Number of steps in the random walk
num_steps = 100

# Generate random walk data
x = [0]
y = [0]
for i in range(num_steps):
    direction = random.choice(['N', 'S', 'E', 'W'])
    if direction == 'N':
        y.append(y[-1] + 1)
        x.append(x[-1])
    elif direction == 'S':
        y.append(y[-1] - 1)
        x.append(x[-1])
    elif direction == 'E':
        x.append(x[-1] + 1)
        y.append(y[-1])
    else:
        x.append(x[-1] - 1)
        y.append(y[-1])

# Plot the random walk
plt.plot(x, y)
plt.title('Random Walk Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
