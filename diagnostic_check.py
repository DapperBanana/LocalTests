
import pandas as pd

# Read the Excel spreadsheet into a pandas DataFrame
df = pd.read_excel('data.xlsx')

# Display the first few rows of the DataFrame
print("First few rows of the data:")
print(df.head())

# Get summary statistics of the data
print("\nSummary statistics:")
print(df.describe())

# Calculate the mean, median, and standard deviation of a specific column
column_name = 'column_name'
mean_value = df[column_name].mean()
median_value = df[column_name].median()
std_dev = df[column_name].std()

print(f"\nMean of {column_name}: {mean_value}")
print(f"Median of {column_name}: {median_value}")
print(f"Standard deviation of {column_name}: {std_dev}")

# Perform other analyses on the data as needed
# For example, calculating correlations, histograms, etc.
