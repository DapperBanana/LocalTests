
import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv('data.csv')

# Extracting x and y values from the data
x = data['Category']
y = data['Value']

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(x, y, color='b')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')
plt.show()
