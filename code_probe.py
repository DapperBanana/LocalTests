
import csv

def read_csv_file(file_name):
    data = []
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data


def analyze_data(data, column):
    total = 0
    count = 0
    for row in data[1:]:
        if row[column].isnumeric():  # Only consider numeric values
            total += int(row[column])
            count += 1
    average = total / count if count != 0 else 0
    return average


def main():
    file_name = input("Enter the CSV file name: ")
    column = input("Enter the column number for analysis (starting from 0): ")

    data = read_csv_file(file_name)
    average = analyze_data(data, int(column))

    print(f"The average value in column {column} is: {average}")


if __name__ == '__main__':
    main()
