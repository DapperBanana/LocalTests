
import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV file
data = pd.read_csv('data.csv')

# Extract x values (categories) and y values (values) from the dataframe
categories = data['Category']
values = data['Value']

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='skyblue')

# Add labels and title
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')

# Show plot
plt.show()
