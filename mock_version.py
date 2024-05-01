
import csv

# Open the CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Find the number of rows and columns in the CSV file
num_rows = len(data)
num_columns = len(data[0])

# Print the data from the CSV file
for row in data:
    print(row)

# Calculate the sum of values in the second column
sum_values = sum([int(row[1]) for row in data])

# Find the maximum and minimum values in the third column
max_value = max([int(row[2]) for row in data])
min_value = min([int(row[2]) for row in data])

# Print the analysis results
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")
print(f"Sum of values in the second column: {sum_values}")
print(f"Maximum value in the third column: {max_value}")
print(f"Minimum value in the third column: {min_value}")
