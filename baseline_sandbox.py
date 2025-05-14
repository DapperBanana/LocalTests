
import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv('data.csv')

# Create a bar chart
plt.bar(data['Category'], data['Value'])
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart of Categories')

# Show the plot
plt.show()
