
import matplotlib.pyplot as plt

# Dictionary of data
data = {"A": 10, "B": 20, "C": 15, "D": 25}

labels = list(data.keys())
values = list(data.values())

plt.bar(labels, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')

plt.show()
