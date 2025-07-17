
import csv

# Open the CSV file for reading
with open('data.csv', 'r') as file:
    reader = csv.reader(file)

    # Read the headers
    headers = next(reader)

    # Initialize variables for analysis
    total_rows = 0
    total_values = 0
    max_value = float('-inf')
    min_value = float('inf')
    sum_values = 0

    # Iterate over each row in the CSV file
    for row in reader:
        total_rows += 1

        # Iterate over each value in the row
        for value in row:
            value = float(value)
            total_values += 1
            sum_values += value

            if value > max_value:
                max_value = value

            if value < min_value:
                min_value = value

    # Calculate the average value
    avg_value = sum_values / total_values

    # Print the analysis results
    print(f"Total number of rows: {total_rows}")
    print(f"Total number of values: {total_values}")
    print(f"Maximum value: {max_value}")
    print(f"Minimum value: {min_value}")
    print(f"Average value: {avg_value}")
