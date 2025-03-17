
import csv

# Open the CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    
    # Skip the header row
    next(reader)
    
    column_index = 1  # Specify the column to analyze (0-based index)
    total = 0
    count = 0
    
    # Iterate over each row in the CSV file
    for row in reader:
        try:
            value = float(row[column_index])
            total += value
            count += 1
        except ValueError:
            # Handle non-numeric values if necessary
            pass
    
    # Calculate the average value
    if count > 0:
        average = total / count
    else:
        average = 0
    
    print(f'Average value of column {column_index}: {average}')
