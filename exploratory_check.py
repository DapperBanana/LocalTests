
import matplotlib.pyplot as plt
import random

# Function to generate random walk data
def random_walk(num_steps):
    x = 0
    y = 0
    walk_x = [x]
    walk_y = [y]

    for _ in range(num_steps):
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

    return walk_x, walk_y

# Generate random walk data
num_steps = 1000
walk_x, walk_y = random_walk(num_steps)

# Plot the random walk
plt.figure(figsize=(10, 6))
plt.plot(walk_x, walk_y, marker='o')
plt.title('Random Walk Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
