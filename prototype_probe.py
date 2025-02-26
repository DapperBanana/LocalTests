
import csv

# Open the CSV file for reading
with open('data.csv', 'r') as file:
    reader = csv.reader(file)

    # Initialize variables for analysis
    total_rows = 0
    total_columns = 0
    max_value = None
    min_value = None
    sum_values = 0

    # Analyze the data
    for row in reader:
        total_rows += 1
        total_columns = max(total_columns, len(row))
        for value in row:
            value = float(value)
            sum_values += value
            if max_value is None or value > max_value:
                max_value = value
            if min_value is None or value < min_value:
                min_value = value
                
    # Output the analysis results
    print(f'Total rows: {total_rows}')
    print(f'Total columns: {total_columns}')
    print(f'Max value: {max_value}')
    print(f'Min value: {min_value}')
    print(f'Sum of all values: {sum_values}')
