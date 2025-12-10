// C# code is not applicable here since the task involves reading CSV and plotting using Python.
// Here's the Python code for your requirement:

import csv
import matplotlib.pyplot as plt

# Read data from CSV
csv_file = 'your_data.csv'  # Replace with your CSV file path
labels = []
values = []

with open(csv_file, 'r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header if present
    for row in reader:
        labels.append(row[0])   # Assuming labels are in the first column
        values.append(float(row[1]))  # Assuming values are in the second column

# Plot bar chart
plt.figure(figsize=(10,6))
plt.bar(labels, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart from CSV Data')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()