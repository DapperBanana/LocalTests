
import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv("data.csv")

# Plot a bar chart
plt.bar(data['Category'], data['Value'])
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')
plt.show()
