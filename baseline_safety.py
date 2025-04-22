
import csv

# Read data from CSV file
data = []
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# Analyze data
total_rows = len(data)
total_columns = len(data[0])

print(f'Total rows: {total_rows}')
print(f'Total columns: {total_columns}')

# Calculate average value in each column
averages = []
for i in range(total_columns):
    column_values = [float(row[i]) for row in data]
    average = sum(column_values) / total_rows
    averages.append(average)
    print(f'Average value in column {i+1}: {average}')

# Calculate sum of all values in the CSV file
total_sum = sum(sum(map(float, row)) for row in data)
print(f'Total sum of all values: {total_sum}')
