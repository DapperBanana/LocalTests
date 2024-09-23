
import csv

def read_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)

if __name__ == "__main__":
    file_path = "your_csv_file.csv"  # Update this with the path to your CSV file
    read_csv_file(file_path)
