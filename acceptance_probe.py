
import csv
import matplotlib.pyplot as plt

# Read data from CSV file
data = []
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# Separate the data into labels and values
labels = [row[0] for row in data[1:]]
values = [int(row[1]) for row in data[1:]]

# Plot bar chart
plt.bar(labels, values)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart from CSV Data')
plt.show()
