
import csv

# Open the CSV file
with open('data.csv') as file:
    reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in reader:
        print(row)
