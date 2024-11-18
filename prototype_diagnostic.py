
import csv
import matplotlib.pyplot as plt

# Read data from CSV file
data = {}
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        key = row[0]
        value = int(row[1])
        data[key] = value

# Plot bar chart
plt.bar(data.keys(), data.values())
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()
