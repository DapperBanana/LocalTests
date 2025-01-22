
import matplotlib.pyplot as plt

# Data
data = {'A': 10, 'B': 15, 'C': 20, 'D': 25}

# Generate bar chart
plt.bar(data.keys(), data.values())

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar Chart')

# Display the chart
plt.show()
