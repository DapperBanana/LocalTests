
import matplotlib.pyplot as plt
import csv

data = {'Category': [], 'Value': []}

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data['Category'].append(row['Category'])
        data['Value'].append(int(row['Value']))

plt.bar(data['Category'], data['Value'])
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')
plt.show()
