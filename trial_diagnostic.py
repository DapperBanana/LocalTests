
import csv
import matplotlib.pyplot as plt

# Read data from CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Extract x and y data from CSV data
x = [row[0] for row in data]
y = [int(row[1]) for row in data]

# Plot bar chart
plt.bar(x, y)
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Category Count Bar Chart')
plt.show()
