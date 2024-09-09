
import csv

# Open the CSV file for reading
with open('data.csv', 'r') as file:
    reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in reader:
        print(row)
