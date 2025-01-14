
import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv('data.csv')

# Extract column data
x = data['Category']
y = data['Value']

# Plot bar chart
plt.bar(x, y)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')
plt.show()
