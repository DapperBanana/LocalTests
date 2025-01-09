
import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv("data.csv")

# Extract x and y values from the data
x_values = data['x']
y_values = data['y']

# Plot bar chart
plt.bar(x_values, y_values)
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Bar Chart')
plt.show()
