
import csv

# Open the CSV file for reading
with open('data.csv', 'r') as file:
    reader = csv.reader(file)

    # Read the header row
    header = next(reader)

    # Calculate the average of a specific column
    total = 0
    count = 0
    for row in reader:
        total += int(row[1])  # Change the index to the desired column
        count += 1

    average = total / count

    print(f'The average of column 1 is: {average}')
