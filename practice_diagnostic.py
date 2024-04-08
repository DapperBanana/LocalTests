
import csv

# Function to read and analyze data from a CSV file
def analyze_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader) # get the header row

        # Initiate variables for analysis
        total_rows = 0
        col_counts = {}

        # Loop through each row in the CSV file
        for row in reader:
            total_rows += 1
            for i, value in enumerate(row):
                col_counts.setdefault(header[i], {}).setdefault(value, 0)
                col_counts[header[i]][value] += 1

        # Print analysis results
        print(f"Total number of rows: {total_rows}")
        print("Column Value Counts:")
        for col, val_counts in col_counts.items():
            print(f"{col}:")
            for val, count in val_counts.items():
                print(f"    {val}: {count}")

# Example usage
analyze_csv('data.csv')
