
import csv

# Function to read and analyze data from a CSV file
def analyze_csv(file):
    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        total = 0
        count = 0
        
        for row in csv_reader:
            value = float(row['value'])
            total += value
            count += 1
        
        if count == 0:
            print("No data found in the CSV file.")
        else:
            average = total / count
            print(f"The average value in the 'value' column is: {average}")
            
# Main program
if __name__ == "__main__":
    file = "data.csv"
    analyze_csv(file)
