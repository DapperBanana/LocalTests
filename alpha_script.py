
import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV file
data = pd.read_csv('data.csv')

# Extract x and y values from data
x = data['Category']
y = data['Value']

# Create bar chart
plt.bar(x, y)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')
plt.show()
