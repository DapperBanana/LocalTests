
import csv

def read_csv(filename):
    # Open the CSV file
    with open(filename, "r") as file:
        # Create a CSV reader object
        reader = csv.reader(file)

        # Read each row in the CSV file
        for row in reader:
            # Print the contents of each row
            print(row)

# Specify the filename of the CSV file
filename = "data.csv"

# Call the function to read and print the CSV file
read_csv(filename)
