
import csv
import matplotlib.pyplot as plt

# Read data from CSV file
data = {}
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data[row['Category']] = int(row['Value'])

# Create bar chart
plt.bar(data.keys(), data.values())
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart of Data')
plt.show()
