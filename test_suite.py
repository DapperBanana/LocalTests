
import csv

def analyze_data(csv_file):
    # Open the CSV file
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        
        # Read and analyze the data
        total_rows = 0
        total_age = 0
        max_age = 0
        min_age = float('inf')
        
        for row in reader:
            total_rows += 1
            age = int(row[1])
            total_age += age
            if age > max_age:
                max_age = age
            if age < min_age:
                min_age = age
        
        average_age = total_age / total_rows
        
        # Print the analysis results
        print(f"Total number of rows: {total_rows}")
        print(f"Average age: {average_age}")
        print(f"Maximum age: {max_age}")
        print(f"Minimum age: {min_age}")

# Specify the CSV file to analyze
csv_file = 'data.csv'

# Call the analyze_data function with the specified CSV file
analyze_data(csv_file)
