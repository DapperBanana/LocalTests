
import matplotlib.pyplot as plt
import random

# Set the number of steps in the random walk
num_steps = 100

# Initialize starting point
x = 0
y = 0

# Lists to store the x and y positions at each step
x_positions = [x]
y_positions = [y]

# Generate random steps
for _ in range(num_steps):
    # Generate a random direction: 0 = up, 1 = down, 2 = left, 3 = right
    direction = random.choice([0, 1, 2, 3])
    
    # Update the x and y positions based on the random direction
    if direction == 0:
        y += 1
    elif direction == 1:
        y -= 1
    elif direction == 2:
        x -= 1
    else:
        x += 1
    
    # Append the new x and y positions to the lists
    x_positions.append(x)
    y_positions.append(y)

# Plot the random walk
plt.figure(figsize=(10, 6))
plt.plot(x_positions, y_positions, marker='o')
plt.title('Random Walk Plot')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.grid(True)
plt.show()
