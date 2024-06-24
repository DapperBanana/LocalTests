
import csv

# Open the CSV file
with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    
    # Read and print each row in the CSV file
    for row in reader:
        print(row)
