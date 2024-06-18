
import pandas as pd
import matplotlib.pyplot as plt

# Load data from a CSV file
data = pd.read_csv('data.csv')

# Extracting data for plotting
x = data['Category']
y = data['Value']

# Creating a bar chart
plt.bar(x, y)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')

# Display the bar chart
plt.show()
