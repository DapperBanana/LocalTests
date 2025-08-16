
import numpy as np
import matplotlib.pyplot as plt

# Generate random walk data
n = 1000
x = np.zeros(n)
y = np.zeros(n)

for i in range(1, n):
    step = np.random.randint(1, 5)
    direction = np.random.randint(1, 5)
    
    if direction == 1:
        x[i] = x[i-1] + step
        y[i] = y[i-1]
    elif direction == 2:
        x[i] = x[i-1] - step
        y[i] = y[i-1]
    elif direction == 3:
        x[i] = x[i-1]
        y[i] = y[i-1] + step
    else:
        x[i] = x[i-1]
        y[i] = y[i-1] - step

# Plot random walk
plt.plot(x, y)
plt.title("Random Walk Plot")
plt.show()
