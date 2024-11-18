
import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv('data.csv')

# Get the x and y values for plotting
x_values = data['Category']
y_values = data['Value']

# Create a bar chart
plt.bar(x_values, y_values)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')
plt.show()
