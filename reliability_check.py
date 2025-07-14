
import matplotlib.pyplot as plt

# Data
data = {'A': 10, 'B': 20, 'C': 15, 'D': 25, 'E': 30}

# Creating bar chart
plt.bar(data.keys(), data.values())

# Adding labels and title
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Simple Bar Chart')

# Displaying the chart
plt.show()
