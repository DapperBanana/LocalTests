
import pandas as pd

# Load the Excel file into a DataFrame
df = pd.read_excel('data.xlsx')

# Display basic information about the DataFrame
print("Columns:")
print(df.columns)
print("\nData Types:")
print(df.dtypes)
print("\nSummary Statistics:")
print(df.describe())

# Perform some analysis on the data
average_age = df['Age'].mean()
max_salary = df['Salary'].max()
min_years_experience = df['YearsExperience'].min()

print("\nAverage Age: ", average_age)
print("Maximum Salary: ", max_salary)
print("Minimum Years of Experience: ", min_years_experience)
