
import csv
import matplotlib.pyplot as plt

# Read data from CSV file
data = []
with open('data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        data.append(row)

# Extract labels and values
labels = [row[0] for row in data[1:]]
values = [int(row[1]) for row in data[1:]]

# Create bar chart
plt.bar(labels, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.xticks(rotation=45)
plt.show()
