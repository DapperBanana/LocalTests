
import pandas as pd

# Read the Excel spreadsheet into a DataFrame
data = pd.read_excel('data.xlsx')

# Display the first few rows of the data
print(data.head())

# Check the data types of each column
print(data.dtypes)

# Perform some basic analysis
print("Summary statistics:")
print(data.describe())

# Calculate the average value of a specific column
average_value = data['column_name'].mean()
print(f"The average value of 'column_name' is: {average_value}")

# Calculate the total sum of a specific column
total_sum = data['column_name'].sum()
print(f"The total sum of 'column_name' is: {total_sum}")
