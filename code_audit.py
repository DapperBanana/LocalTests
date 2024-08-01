
import csv

# Open the CSV file
with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    
    # Read the header row
    headers = next(reader)
    
    # Initialize some variables for analysis
    total_rows = 0
    total_value = 0
    
    # Loop through each row in the CSV file
    for row in reader:
        # Assuming the data we are analyzing is numeric, sum up the values in a specific column
        total_value += int(row[1])
        
        # Count the total number of rows
        total_rows += 1

# Print out some analysis results
print(f"Total rows: {total_rows}")
print(f"Total value: {total_value}")

# Calculate the average value
average_value = total_value / total_rows
print(f"Average value: {average_value}")
