
import csv
import matplotlib.pyplot as plt

# Read data from CSV file
data = []
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# Extract x and y values from data
x = [row[0] for row in data]
y = [int(row[1]) for row in data]

# Plot bar chart
plt.bar(x, y)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart from CSV Data')
plt.show()
