
import csv

filename = "data.csv"

with open(filename, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
