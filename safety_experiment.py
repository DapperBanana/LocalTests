
import pandas as pd

# Load the Excel file using pandas
data = pd.read_excel('data.xlsx')

# Display the first few rows of the data
print("First few rows of the data:")
print(data.head())

# Display basic statistics of the data
print("\nBasic statistics of the data:")
print(data.describe())

# Analyze a specific column
column_name = 'column_name'
column_data = data[column_name]

# Display the mean, median, and mode of the column
print(f"\nAnalysis of column '{column_name}':")
print(f"Mean: {column_data.mean()}")
print(f"Median: {column_data.median()}")
print(f"Mode: {column_data.mode()[0]}")
