
import matplotlib.pyplot as plt

# Dictionary of data
data = {'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]}

# Create a line chart
plt.figure(figsize=(10, 6))
for key, values in data.items():
    plt.plot(values, label=key)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Chart')
plt.legend()
plt.grid(True)
plt.show()
