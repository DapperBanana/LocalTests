
import matplotlib.pyplot as plt

# Dictionary of data
data = {'A': 10, 'B': 20, 'C': 15, 'D': 30}

# Extracting keys and values from the dictionary
keys = list(data.keys())
values = list(data.values())

# Creating a bar chart
plt.bar(keys, values)

# Adding labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart of Data')

# Displaying the bar chart
plt.show()
