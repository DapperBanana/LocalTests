
import matplotlib.pyplot as plt

# Sample data
data = {'A': 10, 'B': 20, 'C': 15, 'D': 25, 'E': 30}

# Create bar chart
plt.bar(data.keys(), data.values())

# Add labels
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')

# Display the chart
plt.show()
