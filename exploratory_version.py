
import csv

def analyze_csv_file(file_name, column_number):
    total = 0
    count = 0

    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # skip header row
        for row in csv_reader:
            try:
                value = float(row[column_number])
                total += value
                count += 1
            except ValueError:
                pass

    if count == 0:
        print("No valid data found in the file.")
    else:
        average = total / count
        print(f"The average value of column {column_number} is: {average}")

file_name = 'data.csv'
column_number = 1  # Assuming the column number to analyze is column 1

analyze_csv_file(file_name, column_number)
