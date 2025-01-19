
import matplotlib.pyplot as plt
import pandas as pd

# Read the data from the CSV file
data = pd.read_csv('data.csv')

# Extract the values from the data
x_values = data['Category']
y_values = data['Value']

# Plot the bar chart
plt.bar(x_values, y_values)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart of Data')
plt.show()
