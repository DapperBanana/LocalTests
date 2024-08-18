
import matplotlib.pyplot as plt
import random

def random_walk(steps):
    x = 0
    y = 0
    walk_x = [x]
    walk_y = [y]

    for _ in range(steps):
        direction = random.choice(['N', 'E', 'S', 'W'])
        if direction == 'N':
            y += 1
        elif direction == 'E':
            x += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'W':
            x -= 1
        walk_x.append(x)
        walk_y.append(y)

    return walk_x, walk_y

steps = 1000
walk_x, walk_y = random_walk(steps)

plt.figure(figsize=(8, 8))
plt.plot(walk_x, walk_y)
plt.scatter(walk_x[0], walk_y[0], color='green', label='Start')
plt.scatter(walk_x[-1], walk_y[-1], color='red', label='End')
plt.title('Random Walk Plot')
plt.legend()
plt.show()
