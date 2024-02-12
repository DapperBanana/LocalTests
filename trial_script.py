
import csv

def analyze_data(csv_file):
    # Open the CSV file
    with open(csv_file, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Skip the header row
        next(csv_reader)
        
        # Initialize variables to store data
        total_rows = 0
        total_value = 0
        
        # Iterate over each row in the file
        for row in csv_reader:
            total_rows += 1
            # Assuming the value you want to analyze is in the first column
            total_value += float(row[0])
        
        # Calculate average
        average_value = total_value / total_rows
        
        # Print the results
        print(f"Total rows: {total_rows}")
        print(f"Total value: {total_value}")
        print(f"Average value: {average_value}")


# Path to the CSV file
csv_file_path = 'data.csv'

# Call the analyze_data function
analyze_data(csv_file_path)
