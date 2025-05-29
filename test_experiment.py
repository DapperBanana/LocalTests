
import csv

# Open the CSV file
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)

    # Loop through each row and print its contents
    for row in csv_reader:
        print(row)
