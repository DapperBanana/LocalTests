
import pandas as pd

# Read data from Excel spreadsheet
df = pd.read_excel('data.xlsx')

# Display basic information about the data
print("Basic Information:")
print(df.info())

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Analyze specific columns
print("\nAnalysis of 'column_name':")
# Replace 'column_name' with the column you want to analyze
print(df['column_name'].value_counts())

# Perform additional analysis here

