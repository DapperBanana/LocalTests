
import csv

# Open the CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header

    # Find the index of the column you want to analyze
    column_name = 'column_name'  # Replace with the name of the column you want to analyze
    column_index = header.index(column_name)

    # Initialize variables for calculating the average
    total = 0
    count = 0

    # Iterate through each row in the CSV file
    for row in reader:
        try:
            value = float(row[column_index])
            total += value
            count += 1
        except ValueError:
            # Skip rows with invalid data
            pass

    # Calculate the average
    if count > 0:
        average = total / count
        print(f'The average of the column "{column_name}" is: {average}')
    else:
        print(f'No valid data found in the column "{column_name}"')
