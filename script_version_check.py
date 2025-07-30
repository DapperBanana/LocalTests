
import csv

# Open the CSV file
with open('data.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Print each row in the CSV file
    for row in csv_reader:
        print(row)
