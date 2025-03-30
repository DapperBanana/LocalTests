
import matplotlib.pyplot as plt
import random

# Number of steps in the random walk
steps = 1000

# Generate the random walk data
x = 0
y = 0
walk_x = [x]
walk_y = [y]

for _ in range(steps):
    direction = random.choice(['up', 'down', 'left', 'right'])
    if direction == 'up':
        y += 1
    elif direction == 'down':
        y -= 1
    elif direction == 'left':
        x -= 1
    elif direction == 'right':
        x += 1
    walk_x.append(x)
    walk_y.append(y)

# Plot the random walk
plt.plot(walk_x, walk_y)
plt.scatter(walk_x[0], walk_y[0], color='green', label='Start')
plt.scatter(walk_x[-1], walk_y[-1], color='red', label='End')
plt.legend()
plt.title('Random Walk Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
