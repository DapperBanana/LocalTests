
import csv

# Open the CSV file
with open('example.csv', 'r') as file:
    csv_reader = csv.reader(file)

    # Loop through each row in the CSV file
    for row in csv_reader:
        print(row)
