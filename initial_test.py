
import pandas as pd

# Load the Excel file
df = pd.read_excel("data.xlsx")

# Display the first few rows of the dataframe
print(df.head())

# Display the summary statistics of the dataframe
print(df.describe())

# Calculate the mean of a specific column
mean_column = df['column_name'].mean()
print(f'Mean of column "column_name": {mean_column}')

# Calculate the median of a specific column
median_column = df['column_name'].median()
print(f'Median of column "column_name": {median_column}')

# Calculate the mode of a specific column
mode_column = df['column_name'].mode()[0]
print(f'Mode of column "column_name": {mode_column}')

# Calculate the standard deviation of a specific column
std_column = df['column_name'].std()
print(f'Standard deviation of column "column_name": {std_column}')
