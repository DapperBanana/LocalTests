
import csv

# Define the file name
file_name = 'data.csv'

# Read the data from the CSV file
data = []
with open(file_name, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# Analyze the data
num_rows = len(data)
num_columns = len(data[0])

print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")

# Calculate the average value in the first column
sum_first_column = sum([int(row[0]) for row in data[1:]])
average_first_column = sum_first_column / (num_rows - 1)
print(f"Average value in the first column: {average_first_column}")

# Calculate the total value in the second column
total_second_column = sum([int(row[1]) for row in data[1:]])
print(f"Total value in the second column: {total_second_column}")
