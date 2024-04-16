
import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV file
data = pd.read_csv('data.csv')

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(data['Category'], data['Value'], color='skyblue')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart of Data')
plt.xticks(rotation=45)
plt.show()
