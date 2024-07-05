
import csv

# Open the CSV file in read mode
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)

    # Loop through each row in the CSV file and print its contents
    for row in csv_reader:
        print(row)
