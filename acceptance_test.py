
import matplotlib.pyplot as plt

# Data
data = {'A': 10, 'B': 20, 'C': 15, 'D': 25}

# Create bar chart
plt.bar(data.keys(), data.values())

# Add labels
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar Chart')

# Show the plot
plt.show()
