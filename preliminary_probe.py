
import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV file
data = pd.read_csv('data.csv')

# Extract data for x-axis and y-axis
x = data['Category']
y = data['Value']

# Create bar chart
plt.bar(x, y)

# Add labels and title
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')

# Show the plot
plt.show()
