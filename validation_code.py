
import csv

# Function to read data from CSV file and perform analysis
def analyze_csv(file_name):
    # Initialize variables to store data
    total_rows = 0
    total_columns = 0
    max_value = None
    min_value = None
    sum_values = 0

    # Open CSV file for reading
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        
        # Loop through rows in CSV file
        for row in csv_reader:
            total_rows += 1
            total_columns = len(row)
            
            # Loop through columns in CSV file
            for value in row:
                try:
                    value = float(value)
                    sum_values += value
                    if max_value is None or value > max_value:
                        max_value = value
                    if min_value is None or value < min_value:
                        min_value = value
                except ValueError:
                    pass

    # Print analysis results
    print(f"Total rows: {total_rows}")
    print(f"Total columns: {total_columns}")
    print(f"Max value: {max_value}")
    print(f"Min value: {min_value}")
    print(f"Sum of all values: {sum_values}")

# Call analyze_csv function with CSV file name
analyze_csv('data.csv')
