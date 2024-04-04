
import csv
import matplotlib.pyplot as plt

# Read data from CSV file
data = {}
with open('data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        data[row[0]] = int(row[1])

# Plot bar chart
plt.bar(data.keys(), data.values())
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()
