
import matplotlib.pyplot as plt

# Sample data
data = {
    'A': 10,
    'B': 20,
    'C': 15,
    'D': 25,
    'E': 30
}

# Create bar chart
plt.bar(data.keys(), data.values())
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Simple Bar Chart')

# Show the chart
plt.show()
