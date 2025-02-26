
import matplotlib.pyplot as plt

# Sample data
data = {'A': 10, 'B': 20, 'C': 15, 'D': 25}

# Create bar chart
plt.bar(range(len(data)), list(data.values()), tick_label=list(data.keys()))
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart of Data')

# Show plot
plt.show()
