
import csv

# Open the CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    
    # Loop through each row in the file and print its contents
    for row in reader:
        print(row)
