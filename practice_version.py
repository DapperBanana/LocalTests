
import matplotlib.pyplot as plt

# Dictionary of data
data = {
    'January': 10,
    'February': 20,
    'March': 15,
    'April': 25,
    'May': 30
}

# Extracting x and y values from the dictionary
months = list(data.keys())
values = list(data.values())

# Creating the line chart
plt.figure(figsize=(8, 6))
plt.plot(months, values, marker='o', color='b', linestyle='-', linewidth=2)

# Adding labels and title
plt.xlabel('Months')
plt.ylabel('Values')
plt.title('Simple Line Chart')

# Displaying the chart
plt.grid(True)
plt.show()
