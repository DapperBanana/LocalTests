
import csv

file_name = "data.csv"

# Open the CSV file
with open(file_name, 'r') as file:
    csv_reader = csv.reader(file)
    
    # Loop through each row and print its contents
    for row in csv_reader:
        print(row)
