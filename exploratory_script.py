
import csv

# Function to read data from CSV file and print it
def read_csv_file(file_name):
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        
        # Skip the header row
        next(csv_reader)
        
        # Print each row in the CSV file
        for row in csv_reader:
            print(row)

# Function to analyze data from CSV file
def analyze_csv_file(file_name):
    total_rows = 0
    total_amount = 0
    
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        
        # Skip the header row
        next(csv_reader)
        
        # Analyze each row in the CSV file
        for row in csv_reader:
            total_rows += 1
            total_amount += float(row[1])
    
    # Print analysis results
    print("Total number of rows:", total_rows)
    print("Total amount:", total_amount)

# Main function
if __name__ == "__main__":
    file_name = "data.csv"
    
    # Read and print data from CSV file
    read_csv_file(file_name)
    
    # Analyze data from CSV file
    analyze_csv_file(file_name)
