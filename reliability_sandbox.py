
import csv

# Open the CSV file for reading
with open('example.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    # Iterate over each row in the CSV file
    for row in csvreader:
        print(row)
